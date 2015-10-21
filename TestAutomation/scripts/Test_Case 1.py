import sys
from mercurial import progress


print "Test Number 1"
print "Correct Time Output"
print "Component: Progress.py"
print "Method: fmtremaining( (int) seconds )"
print "Input: 100"
print "Expected output: 1m40s"
outcome = progress.fmtremaining(100) == '1m40s'
print "Outcome:", outcome
