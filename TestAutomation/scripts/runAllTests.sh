#!/bin/bash

# Removes all prior results of tests
rm ~/RedTeam/TestAutomation/reports/*

# Prints HTML Header and body tag
echo "<HTML>" >> ~/RedTeam/TestAutomation/reports/report.html
echo "<body>" >> ~/RedTeam/TestAutomation/reports/report.html

# Prints title
echo -e "<h1 style="color:red"> Red Team - Mercurial Project: Test Output </h1>\n\n" >> ~/RedTeam/TestAutomation/reports/report.html

# Initializing the variables for looping through the test files (FILES) and test number (testNum)
FILES=~/RedTeam/TestAutomation/testCasesExecutables/*
testNum=1

# A loop which runs through the files in the scripts directory
for f in $FILES

do
	echo -e "<p>Test Number $testNum \n" >> ~/RedTeam/TestAutomation/reports/report.html
	echo -e "$f </p>\n" >> ~/RedTeam/TestAutomation/reports/report.html
	bash $f

	# Carriage return to a new line and increment the value of testNum
	echo -e "\n" >> ~/RedTeam/TestAutomation/reports/report.html
	((testNum++))
done

echo "</body>" >> ~/RedTeam/TestAutomation/reports/report.html
echo "</HTML>" >> ~/RedTeam/TestAutomation/reports/report.html
