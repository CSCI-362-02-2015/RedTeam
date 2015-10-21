import sys
from mercurial import templatefilters

print "Test Number 4"
print "Count the number of items in a list or string"
print "Component: templatefilters.py"
print "Method: count(string/list)"
print "Input: 'abcde'"
print "Expected Output: 5"
outcome = templatefilters.count('abcde')
print "Outcome:", outcome
