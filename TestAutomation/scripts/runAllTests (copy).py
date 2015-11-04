# runAllTests.py

def main():
	import os

	#prepare import statements
	import_base = "from mercurial import "

	#Change working directory to testCasesExecutables
	path = os.path.expanduser("~/RedTeam/TestAutomation/testCasesExecutables/")
	os.chdir(path)

	#Read each file

		#Print out relative test information

		#Execute test file script
		import_module = import_base + module
		exec( import_module )
		statement = module + "." + function + "(" + cast + case_input + ")"
		exec(statement)
