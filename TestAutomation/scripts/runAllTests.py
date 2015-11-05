# runAllTests.py

import os, sys
import glob

#Change working directory to testCasesExecutables

#path = os.path.expanduser("~/RedTeam/TestAutomation/testCases/")
path = os.getcwd() 
path = os.path.abspath(os.path.join(path, os.pardir)) + "/testCases"



os.chdir(path) 
listing = os.listdir(path)
listing.sort()
import_base = "from mercurial import "

#Counts the test cases in the testCases folder
count = len(listing)

#If statement to check if the folder has test cases
if count < 1:
        print "There are no test cases.  Be Better..."
else:
        passCount = 0 #number of passed tests
        failCount = 0 #numer of failed tests
        
        for infile in listing:
                #print "Current File: " + infile
                try:
                        with open(path + '/' + infile) as f:
                                testList = f.read().splitlines()
                        iden = testList[0]
                        req = testList[1]
                        component = testList[2]
                        method = testList[3]
                        inp = testList[4]
                        outcome = testList[5]

                        print "ID: ", iden

                        

                        #Execute test file script
                
                        import_module = import_base + component
                        exec( import_module )
                        
                        print "Requirements: ", req
                        print "Component: ", component
                        print "Method: ", method
                        print "Input: ", inp
                        print "Expected Outcome: ", outcome
                        statement = 'print(' + component + "." + method + "(" + inp + ")" + ")"
                        exec(statement)
                        passCount += 1
                except:
                        failCount += 1
                        e = sys.exc_info()[0]
                        print "Unable to execute TestID[" + iden +"]"
                        print "Please check formatting and inputs of test case"
                        print(e)
                        print 
                        print "Continuing..."
                
                print('\n')

        print "Number of Tests: " + str(count)
        print "Passed: " + str(passCount)
        print "Failed: " + str(failCount) + "\n"
        print "Done"

        
