from mercurial import progress

import sys

testVal = int(sys.argv[1])
oracleVal = str(sys.argv[2])

outcome = progress.fmtremaining(testVal) == oracleVal

if outcome:
	print 'PASS'
else:
	print 'FAIL'