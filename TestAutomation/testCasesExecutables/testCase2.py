from mercurial import simplemerge

import sys
oracleVal = (50,100)

outcome = simplemerge.intersect( (0,100),(50,150) ) == oracleVal

if outcome:
	print 'PASS'
else:
	print 'FAIL'
