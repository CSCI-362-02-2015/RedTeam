#!/usr/bin/python

# runAllTests.py

import os, sys, glob, StringIO, contextlib


#Change working directory to testCasesExecutables

@contextlib.contextmanager
def stdoutIO(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = StringIO.StringIO()
		sys.stdout = stdout
		yield stdout
		sys.stdout = old

	


def main():
  #testCasePath = os.testCasePath.expanduser("~/RedTeam/TestAutomation/testCases/")
  path = os.getcwd() 
  testCasePath = os.path.abspath(os.path.join(path, os.pardir, "testCases"))
  reportPath = os.path.abspath(os.path.join(path, os.pardir, "reports/report.html"))
  os.chdir(testCasePath) 
  listing = os.listdir(testCasePath)
  listing.sort()
  import_base = "from mercurial import "

  #Counts the test cases in the testCases folder
  count = len(listing)

  writeOpeningInfo(reportPath)
  report = open(reportPath, 'a+')



  #If statement to check if the folder has test cases
  if count < 1:
    report.write("No test cases found in test directory")
    print "There are no test cases.  Be Better..."
  else:
          passCount = 0 #number of passed tests
          failCount = 0 #numer of failed tests
          
          for infile in listing:
                  #print "Current File: " + infile
                  try:
                          with open(testCasePath + '/' + infile, 'r') as f:
                                  testList = f.read().splitlines()
                          iden = testList[0]
                          req = testList[1]
                          component = testList[2]
                          method = testList[3]
                          inp = testList[4]
                          outcome = testList[5]

                          print "ID: ", iden

                          passFormat = '<tr bgcolor="#00FF00"><td>{}</td><td>{}</td><td>TODO</td><td>{}</td><td>{}</td></tr>'
                          failFormat = '<tr bgcolor ="#FF0000"><td>{}</td><td>{}</td><td>Outcome</td><td>{}</td><td>{}</td></tr>'

                          #Execute test file script
                  
                          import_module = import_base + component
                          exec( import_module )
                          
##                          print "Requirements: ", req
##                          print "Component: ", component
##                          print "Method: ", method
##                          print "Input: ", inp
##                          print "Expected Outcome: ", outcome
                          
                          statement = 'print(' + component + "." + method + "(" + inp + ")" + ")"
                          ##statement = 'print(' + component + "." + method + "(" + inp + ")" + "> testing.txt)"
                          

                          
##                          code = compile(statement, "script", "exec")

                          
                          print exec(statement).stdoutIO().getValue()

                          


                          
                          passCount += 1
                          passFormat = passFormat.format(iden, inp, outcome, "PASS")
                          report.write(passFormat)
                  except:
                          failCount += 1
                          failFormat = failFormat.format(iden, inp, outcome, "FAIL")
                          report.write(failFormat)
                          e = sys.exc_info()[0]
                          print "Unable to execute TestID[" + iden + "]"
                          print "Please check formatting and inputs of test case"
                          print(e)
                          print 
                          print "Continuing..."
                  
                  print('\n')

                  
          f.close()
          report.write("</table>")
          report.write("</br></brb>Number of Tests: " + str(count) + "</br>")
          report.write("Passed: " + str(passCount) + "</br>")
          report.write("Failed: " + str(failCount))
          report.write("</body></html>")
          report.close()
          printSummary(count, passCount, failCount)

def writeOpeningInfo(reportPath):
  
  report = open(reportPath, 'w+')
  report.write("<!DOCTYPE html>")
  report.write("<html>")
  report.write("<body>")
  report.write('<table border="1" style =""width:100%>')
  report.write("<tr>")
  report.write("<td><b>Test ID</b></td>")
  report.write("<td><b>Input</b></td>")
  report.write("<td><b>Output</b></td>")
  report.write("<td><b>Expected</b></td>")
  report.write("<td><b>Pass/Fail</b></td>")
  report.close()


def printSummary(count, passCount, failCount):
  #Print Stats at the end        
  print "Number of Tests: {}".format(count)
  print "Passed: {}".format(passCount)
  print "Failed: {}\n".format(failCount)
  print "Done"




if __name__ == "__main__":
  main()










  
