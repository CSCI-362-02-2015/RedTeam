# demandimport.py - global demand-loading of modules for Mercurial
#
# Copyright 2006, 2007 Matt Mackall <mpm@selenic.com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

'''
demandimport - automatic demandloading of modules

To enable this module, do:

  import demandimport; demandimport.enable()

Imports of the following forms will be demand-loaded:

  import a, b.c
  import a.b as c
  from a import b,c # a will be loaded immediately

These imports will not be delayed:

  from a import *
  b = __import__(a)
'''

from __future__ import absolute_import

import contextlib
import os
import sys

# __builtin__ in Python 2, builtins in Python 3.
try:
    import __builtin__ as builtins
except ImportError:
    import builtins

contextmanager = contextlib.contextmanager

_origimport = __import__

nothing = object()

# Python 3 doesn't have relative imports nor level -1.
level = -1
if sys.version_info[0] >= 3:
    level = 0
_import = _origimport

def _hgextimport(importfunc, name, globals, *args, **kwargs):
    try:
        return importfunc(name, globals, *args, **kwargs)
    except ImportError:
        if not globals:
            raise
        # extensions are loaded with "hgext_" prefix
        hgextname = 'hgext_%s' % name
        nameroot = hgextname.split('.', 1)[0]
        contextroot = globals.get('__name__', '').split('.', 1)[0]
        if nameroot != contextroot:
            raise
        # retry to import with "hgext_" prefix
        return importfunc(hgextname, globals, *args, **kwargs)

class _demandmod(object):
    """module demand-loader and proxy"""
    def __init__(self, name, globals, locals, level=level):
        if '.' in name:
            head, rest = name.split('.', 1)
            after = [rest]
        else:
            head = name
            after = []
        object.__setattr__(self, "_data",
                           (head, globals, locals, after, level))
        object.__setattr__(self, "_module", None)
    def _extend(self, name):
        """add to the list of submodules to load"""
        self._data[3].append(name)
    def _load(self):
        if not self._module:
            head, globals, locals, after, level = self._data
            mod = _hgextimport(_import, head, globals, locals, None, level)
            # load submodules
            def subload(mod, p):
                h, t = p, None
                if '.' in p:
                    h, t = p.split('.', 1)
                if getattr(mod, h, nothing) is nothing:
                    setattr(mod, h, _demandmod(p, mod.__dict__, mod.__dict__))
                elif t:
                    subload(getattr(mod, h), t)

            for x in after:
                subload(mod, x)

            # are we in the locals dictionary still?
            if locals and locals.get(head) == self:
                locals[head] = mod
            object.__setattr__(self, "_module", mod)

    def __repr__(self):
        if self._module:
            return "<proxied module '%s'>" % self._data[0]
        return "<unloaded module '%s'>" % self._data[0]
    def __call__(self, *args, **kwargs):
        raise TypeError("%s object is not callable" % repr(self))
    def __getattribute__(self, attr):
        if attr in ('_data', '_extend', '_load', '_module'):
            return object.__getattribute__(self, attr)
        self._load()
        return getattr(self._module, attr)
    def __setattr__(self, attr, val):
        self._load()
        setattr(self._module, attr, val)

def _demandimport(name, globals=None, locals=None, fromlist=None, level=level):
    if not locals or name in ignore or fromlist == ('*',):
        # these cases we can't really delay
        return _hgextimport(_import, name, globals, locals, fromlist, level)
    elif not fromlist:
        # import a [as b]
        if '.' in name: # a.b
            base, rest = name.split('.', 1)
            # email.__init__ loading email.mime
            if globals and globals.get('__name__', None) == base:
                return _import(name, globals, locals, fromlist, level)
            # if a is already demand-loaded, add b to its submodule list
            if base in locals:
                if isinstance(locals[base], _demandmod):
                    locals[base]._extend(rest)
                return locals[base]
        return _demandmod(name, globals, locals, level)
    else:
        # There is a fromlist.
        # from a import b,c,d
        # from . import b,c,d
        # from .a import b,c,d

        # level == -1: relative and absolute attempted (Python 2 only).
        # level >= 0: absolute only (Python 2 w/ absolute_import and Python 3).
        # The modern Mercurial convention is to use absolute_import everywhere,
        # so modern Mercurial code will have level >= 0.

        if level >= 0:
            # Mercurial's enforced import style does not use
            # "from a import b,c,d" or "from .a import b,c,d" syntax. In
            # addition, this appears to be giving errors with some modules
            # for unknown reasons. Since we shouldn't be using this syntax
            # much, work around the problems.
            if name:
                return _hgextimport(_origimport, name, globals, locals,
                                    fromlist, level)

            mod = _hgextimport(_origimport, name, globals, locals, level=level)
            for x in fromlist:
                # Missing symbols mean they weren't defined in the module
                # itself which means they are sub-modules.
                if getattr(mod, x, nothing) is nothing:
                    setattr(mod, x,
                            _demandmod(x, mod.__dict__, locals, level=level))

            return mod

        # But, we still need to support lazy loading of standard library and 3rd
        # party modules. So handle level == -1.
        mod = _hgextimport(_origimport, name, globals, locals)
        # recurse down the module chain
        for comp in name.split('.')[1:]:
            if getattr(mod, comp, nothing) is nothing:
                setattr(mod, comp,
                        _demandmod(comp, mod.__dict__, mod.__dict__))
            mod = getattr(mod, comp)
        for x in fromlist:
            # set requested submodules for demand load
            if getattr(mod, x, nothing) is nothing:
                setattr(mod, x, _demandmod(x, mod.__dict__, locals))
        return mod

ignore = [
    '__future__',
    '_hashlib',
    '_xmlplus',
    'fcntl',
    'win32com.gen_py',
    '_winreg', # 2.7 mimetypes needs immediate ImportError
    'pythoncom',
    # imported by tarfile, not available under Windows
    'pwd',
    'grp',
    # imported by profile, itself imported by hotshot.stats,
    # not available under Windows
    'resource',
    # this trips up many extension authors
    'gtk',
    # setuptools' pkg_resources.py expects "from __main__ import x" to
    # raise ImportError if x not defined
    '__main__',
    '_ssl', # conditional imports in the stdlib, issue1964
    'rfc822',
    'mimetools',
    # setuptools 8 expects this module to explode early when not on windows
    'distutils.msvc9compiler'
    ]

def isenabled():
    return builtins.__import__ == _demandimport

def enable():
    "enable global demand-loading of modules"
    if os.environ.get('HGDEMANDIMPORT') != 'disable':
        builtins.__import__ = _demandimport

def disable():
    "disable global demand-loading of modules"
    builtins.__import__ = _origimport

@contextmanager
def deactivated():
    "context manager for disabling demandimport in 'with' blocks"
    demandenabled = isenabled()
    if demandenabled:
        disable()

    try:
        yield
    finally:
        if demandenabled:
            enable()
