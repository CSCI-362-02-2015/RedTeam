#!/bin/bash

# Template test script

# Print test title
echo "TEST NAME" >> ~/RedTeam/TestAutomation/temp/output.txt
echo "Requirement: REQUIREMENT" >> ~/RedTeam/TestAutomation/temp/output.txt
echo "COMPONENT / METHOD " >> ~/RedTeam/TestAutomation/temp/output.txt
echo "Test Input: INPUT  " >> ~/RedTeam/TestAutomation/temp/output.txt
# OPTIONAL (CL ARGUMENTS)
echo "(CL ARGUMENTS)"
echo "Expected Outcome: OUTCOME" >> ~/RedTeam/TestAutomation/temp/output.txt

### PYTHON SCRIPT
#python (file name) (any arugments)
# HOW TO RETURN A VALUE (FOR COMPARISON AGAINST ORACLE)
# import sys
# AT END OF PYTHON SCRIPT
#
## sys.stdout.write('Bugs: 5|Other: 10\n')
## sys.stdout.flush()
## sys.exit(0)

echo #PASS OR FAIL
