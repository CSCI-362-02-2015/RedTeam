#CSCI 362 Group Project
#RED TEAM
#Kyle Brooks
#Jesse Hunt
#Chris Sigmund

#!/usr/bin/python

# runAllTests.py

import os, sys, glob, StringIO, contextlib, webbrowser


path = os.getcwd() 
testCasePath = os.path.abspath(os.path.join(path, os.pardir, "testCases"))
reportPath = os.path.abspath(os.path.join(path, os.pardir, "reports/report.html"))
os.chdir(testCasePath) 
listing = os.listdir(testCasePath)
listing.sort()
import_base = "from mercurial import "



def main():

        
  #Counts the test cases in the testCases folder
  count = len(listing)
  writeOpeningHTML()
  report = open(reportPath, 'a+')

  #If statement to check if the folder has test cases
  if count < 1:
     report.write("No test cases found in test directory")
     report.close()
     print "There are no test cases.  Be Better..."
  else:
     runTests(report, count)
     webbrowser.get('Firefox').open(reportPath)

def runTests(report, count):

        passCount = 0 #number of passed tests
        failCount = 0 #numer of failed tests
          
        for infile in listing:
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
                                
                                passFormat = '<tr bgcolor="#00FF00"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'
                                failFormat = '<tr bgcolor ="#FF0000"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'


                                #Execute test file script
                                import_module = import_base + component
                                exec( import_module )
                                print "Requirements: ", req
                                print "Component: ", component
                                print "Method: ", method
                                print "Input: ", inp
                                print "Expected Outcome: ", outcome


                                statement = component + "." + method+  "(" + inp + ")"
                                result = eval(statement)
                                print "Result: " + str(result)
                                


                                if (str(result) == str(outcome)):
                                        passCount += 1
                                        passFormat = passFormat.format(iden, inp, outcome, str(result), "PASS")
                                        report.write(passFormat)
                                        print("PASS\n")
                                else:
                                        failCount += 1
                                        failFormat = failFormat.format(iden, inp, outcome, str(result), "FAIL")
                                        report.write(failFormat)
                                        print("FAIL\n")
                except:
                        failCount += 1
                        failFormat = failFormat.format(iden, inp, outcome, "ERROR", "FAIL")
                        report.write(failFormat)
                        e = sys.exc_info()[0]
                        print "Unable to execute TestID[" + iden + "]"
                        print "Please check formatting and inputs of test case"
                        print(e)
                        print "Continuing..."
                        print('\n')
        f.close()

        writeClosingHTML(report, count, passCount, failCount)
        printSummary(count, passCount, failCount)

def writeOpeningHTML():
  
  report = open(reportPath, 'w+')
  report.write("<!DOCTYPE html>")
  report.write("<html>")
  report.write("<body>")
  report.write('<table border="1" style =""width:100%>')
  report.write("<tr>")
  report.write("<td><b>Test ID</b></td>")
  report.write("<td><b>Input</b></td>")
  report.write("<td><b>Expected Output</b></td>")
  report.write("<td><b>Actual Output</b></td>")
  report.write("<td><b>Pass/Fail</b></td>")
  report.close()


def writeClosingHTML(report, count, passCount, failCount):
  report.write("</table>")
  report.write("</br></brb>Number of Tests: " + str(count) + "</br>")
  report.write("Passed: " + str(passCount) + "</br>")
  report.write("Failed: " + str(failCount))
  report.write("</body></html>")
  report.close()


def printSummary(count, passCount, failCount):
  #Print Stats at the end     
  print "Number of Tests: {}".format(count)
  print "Passed: {}".format(passCount)
  print "Failed: {}\n".format(failCount)
  print "Done"






if __name__ == "__main__":
  main()










  
