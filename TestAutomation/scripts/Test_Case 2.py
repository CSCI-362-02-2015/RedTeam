Inimport sys
from mercurial import simplemerge

print "Test Number 2"
print "Intersection of two ranges"
print "Component: simplemerge.py"
print "Method: intersect((int, int),(int, int)) "
print "Input: ((0,100),(50,150))"
print "Expected Output: (50,100) "
outcome = simplemerge.intersect((0,100),(50,150))
print "Outcome:", outcome
