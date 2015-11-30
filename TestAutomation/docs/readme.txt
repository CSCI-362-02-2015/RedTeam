Readme for for Red Team's Mercurial project

1. Building Mercurial

	To build Mercurial, follow the steps below. 
	** If you are changing the source code, you must also follow the below steps before the test script will execute the altered code. **

		i.Install Python developer module

			$ sudo apt-get install python-dev

		ii. Navigate to the /src directory. From there, execute the build using the following command:

			$ sudo make install

2. Running the test script

	Navigate to the /scripts directory
	Execute the following code:

		$ python runAllTests.py

3. Creating a test case

	To create a test case, you must create a .txt file in the /testCases directory. The test cases execute in alphanumeric order based on file name, so be aware the label you attribute to the text may not match up with the file name.

		i. Create .txt file in /testCases
		ii. Enter information in the following order:
			Line 1: Test Label (text or number, given test cases are all numbers)
			Line 2: Description of what the method the test is using and its function
			Line 3: Component (.py file, just the file name, no extension)
			Line 4: Method
			Line 5: Input
			Line 6: Expected Output (Exactly as the IDE would display it)

