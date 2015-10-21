import sys
from mercurial import worker

print "Test Number 3"
print "Count the number of CPU's"
print "Component: worker.py"
print "Method: countcpus()"
print "Input: none"
print "Expected Output: 1"
outcome = worker.countcpus()
print "Outcome:", outcome
