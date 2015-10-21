from mercurial import worker

import sys

oracleVal = str(sys.argv[1])

outcome = worker.countcpus() == oracleVal


if outcome:
	print 'PASS'
else:
	print 'FAIL'
