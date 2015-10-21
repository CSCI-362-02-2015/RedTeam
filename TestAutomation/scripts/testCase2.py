from mercurial import simplemerge

import sys

testVal = int(sys.argv[1])
oracleVal = str(sys.argv[2])

outcome = simplermerge.intersect( (0,100),(50,150) ) == oracleVal

if outcome:
	print 'PASS'
else:
	print 'FAIL'
