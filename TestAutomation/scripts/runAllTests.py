# runAllTests.py

import os
import glob

#Change working directory to testCasesExecutables
#path = os.path.expanduser("~/RedTeam/TestAutomation/testCasesExecutables/")
#os.chdir(path)

path = os.path.abspath('testCases')
listing = os.listdir(path)

#Counts the test cases in the testCases folder
count = len(listing)

#If statement to check if the folder has test cases
if count < 1:
	print "There are no test cases.  Be Better..."
else:
	for infile in listing:
		print "Current File: " + infile
	
		f = open(path + '/' + infile)
		line1 = f.readline()
		line2 = f.readline()
		line3 = f.readline()
		line4 = f.readline()
		line5 = f.readline()
		line6 = f.readline()

		print "ID: ", line1
		print "Requirements: ", line2
		print "Component: ", line3
		print "Method: ", line4
		print "Input: ", line5
		print "Expected Outcome: ", line6
		
		print('\n')

	#Execute test file script
