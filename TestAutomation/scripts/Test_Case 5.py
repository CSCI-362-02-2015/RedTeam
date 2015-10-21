import sys
from mercurial import namespaces

print "Test Number 5"
print "Concatenates elements into a list"
print "Component: namespaces.py"
print "Method: tolist( String []items) "
print "Input: '1' '2' '3' '4'"
print "Expected Output: ['1234'] "
outcome = namespaces.tolist('1' '2' '3' '4')
print "Outcome:", outcome
