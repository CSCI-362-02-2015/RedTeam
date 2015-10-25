#!/bin/bash

# Removes all prior results of tests
##rm ~/RedTeam/TestAutomation/reports/*

# Prints HTML Header and body tag
##echo "<HTML>" >> ~/RedTeam/TestAutomation/reports/report.html
##echo "<body>" >> ~/RedTeam/TestAutomation/reports/report.html

# Prints title
##echo -e "<h1 style="color:red"> Red Team - Mercurial Project: Test Output </h1>\n\n" >> ~/RedTeam/TestAutomation/reports/report.html

# Initializing the variables for looping through the test files (FILES) and test number (testNum)
FILES=~/RedTeam/TestAutomation/testCases/*

# A loop which runs through the files in the scripts directory
for f in $FILES; do

	echo $RANDOM % 10 + 1 | bc

	read -r script
	echo $script
	
	while read -r line; do
		echo $line
	done < "$f"

	## bash $f >> ~/RedTeam/TestAutomation/reports/report.html

	# Carriage return to a new line and increment the value of testNum
	## echo -e "\n" >> ~/RedTeam/TestAutomation/reports/report.html
	eval $script
	
	exit
done

##echo "</body>" >> ~/RedTeam/TestAutomation/reports/report.html
##echo "</HTML>" >> ~/RedTeam/TestAutomation/reports/report.html
