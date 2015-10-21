#!/bin/bash

# Removes all prior results of tests
rm ~/RedTeam/TestAutomation/temp/*

# Prints title
echo -e "Red Team - Mercurial Project: Test Output\n\n" >> ~/RedTeam/TestAutomation/temp/output.txt

# Initializing the variables for looping through the test files (FILES) and test number (testNum)
FILES=~/RedTeam/TestAutomation/scripts/*
testNum=1

# A loop which runs through the files in the scripts directory
for f in $FILES

do
	echo -e "Test Number $testNum \n" >> ~/RedTeam/TestAutomation/temp/output.txt
	echo "$f" >> ~/RedTeam/TestAutomation/temp/output.txt

	# Carriage return to a new line and increment the value of testNum
	echo -e "\n" >> ~/RedTeam/TestAutomation/temp/output.txt
	((testNum++))
done
