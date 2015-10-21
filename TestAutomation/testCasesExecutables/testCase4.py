from mercurial import templatefilters

import sys

testVal = str(sys.argv[1])
oracleVal = int(sys.argv[2])

outcome = templatefilters.count(testVal) == oracleVal

if outcome:
	print "PASS"
else:
	print "FAIL"
