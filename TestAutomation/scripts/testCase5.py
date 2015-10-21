from mercurial import namespaces

import sys

testVal = int(sys.argv[1])
oracleVal = str(sys.argv[2])

outcome = namespaces.tolist('1' '2' '3' '4') == oracleVal

if outcome:
	print 'PASS'
else:
	print 'FAIL'

