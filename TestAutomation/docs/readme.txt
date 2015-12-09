Readme for for Red Team's Mercurial project

1. Building Mercurial

	To build Mercurial, follow the steps below (in terminal). 
	** If you are changing the source code, you must also follow the below steps before the test script will execute the altered code. **

		i.  Download repo of Mercurial (mercurial-scm.org).  Extract files to the RedTeam folder.

		ii. Install Python developer module

			sudo apt-get install python-dev

		iii.  Navigate to the mercurial-3.6.2/ directory through the RedTeam folder. From there, execute the build using the following command:

			$ sudo make install


2. Running the test script

	25 test cases have already been created. To run these tests:

	In terminal, navigate to the /scripts directory
	Execute the following code:

		$ python runAllTests.py

3. Creating a test case

	To create a test case, you must create a .txt file in the /testCases directory. The test cases execute in alphanumeric order based on file name, so be aware the label you attribute to the text may not match up with the file name. A sample test case template can be found under TestAutomation/docs/testCase_TEMPLATE.txt. Overview instructions can be found below.

		i. Create .txt file in /testCases
		ii. Enter information in the following order:
			Line 1: Test Label (text or number, given test cases are all numbers)
			Line 2: Description of what the method the test is using and its function
			Line 3: Component (.py file, just the file name, no extension)
			Line 4: Method
			Line 5: Input
			Line 6: Expected Output (Exactly as the IDE would display it)


4. Editing the source code.

	The source code files are saved in the Python library.  To access these files you must go to files on the task bar. Then go to computer.  In computer go the 'usr' folder.  In the usr folder go to the 'local' folder.  In the local folder go to the 'lib' folder.  In the lib folder go to the 'python2.7' folder.  In the python2.7 folder go to the 'dist-packages' folder.  In the dist-packages folder go to the mercurial folder.  This is where the files to edit are located.

	/usr/local/lib/python2.7/dist-packages/mercurial/

	After navigating to the mercurial folder, you will need to modify the permissions of the files that are to be edited.

		While in the mercurial folder, execute the following commands one at a time: 

			sudo chown <user> progress.py
			sudo chown <user> namespaces.py
			sudo chown <user> templatefilters.py
			sudo chown <user> simplemerge.py
			sudo chown <user> worker.py



