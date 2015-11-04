# runAllTests.py

import os
import glob

#Change working directory to testCasesExecutables
path = os.path.expanduser("~/RedTeam/TestAutomation/testCases/")
os.chdir(path)
listing = os.listdir(path)
import_base = "from mercurial import "

#Counts the test cases in the testCases folder
count = len(listing)

#If statement to check if the folder has test cases
if count < 1:
	print "There are no test cases.  Be Better..."
else:
	for infile in listing:
		print "Current File: " + infile
	
		with open(path + '/' + infile) as f:
			testList = f.read().splitlines()
		iden = testList[0]
		req = testList[1]
		component = testList[2]
		method = testList[3]
		inp = testList[4]
		outcome = testList[5]

		print "ID: ", iden
		print "Requirements: ", req
		print "Component: ", component
		print "Method: ", method
		print "Input: ", inp
		print "Expected Outcome: ", outcome

		#Execute test file script
		import_module = import_base + component
		exec( import_module )
		statement = 'print(' + component + "." + method + "(" + inp + ")" + ")"
		exec(statement)
		
		print('\n')

	#Execute test file script
