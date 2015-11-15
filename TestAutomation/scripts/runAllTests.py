#!/usr/bin/python

#CSCI 362 Group Project
#RED TEAM
#Kyle Brooks
#Jesse Hunt
#Chris Sigmund

'''
The purpose of this script is to test functions implemented in the
OSS Mercurial. The script reads .txt files located in
the folder RedTeam/TestAutomation/testCases and uses the information from
them to compile and run a test case. The test case files contain the name
of the class and method to be tested, as well as the input given. The value
returned by the eval command is checked against an oracle value inside the
test case text file.


To write test cases, follow the instructions in the
README.txt file, located in /RedTeam/
'''


import os, sys, glob, StringIO, contextlib, webbrowser

# Global variables, to cut down on parameter passing
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
     openReport()

  print("Done")


#runTests is where the lion's share of the work is done
#it reads in each test case file individually, compiles
#and runs the code, then evaluates this against the oracle value
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
                                compAndMethod = component + "." + method + "()"
                                
                                print "ID: ", iden


                                ##Format: TestID, Component/Method, Input, Expected Output, Actual Output, Pass/Fail
                                passFormat = '<tr bgcolor="#00FF00"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'   
                                failFormat = '<tr bgcolor ="#FF0000"><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'


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
                                        passFormat = passFormat.format(iden, compAndMethod, inp, outcome, str(result), "PASS")
                                        report.write(passFormat)
                                        print("PASS\n")
                                else:
                                        failCount += 1
                                        failFormat = failFormat.format(iden, compAndMethod, inp, outcome, str(result), "FAIL")
                                        report.write(failFormat)
                                        print("FAIL\n")
                except:
                        failCount += 1
                        failFormat = failFormat.format(iden, compAndMethod, inp, outcome, "ERROR", "FAIL")
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
  report.write("<head>")
  report.write("<style>")
  report.write("table, th, td {border: 1px solid black; border-collapse: collapse;}")
  report.write("</style></head>")
  report.write("<body>")
  report.write('<table border="1" style =""width:100%>')
  report.write("<tr>")
  report.write("<td><b>Test ID</b></td>")
  report.write("<td><b>Component.method()</b></td>")
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

#May not be the most elegant way of doing things
#assumes user has Chrome installed
#otherwise attempts to open Firefox
def openReport():
  try:
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(reportPath)
  except:
    webbrowser.get('Firefox').open(reportPath)
    


if __name__ == "__main__":
  main()










  
