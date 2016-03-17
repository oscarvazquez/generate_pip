import sys
from generate import *

class main: 
	def __init__(self):
		if len(sys.argv) > 1:
			self.check_packages()
		else:
			print 'No parameters given, available function \n \t new <pip_module_name>'

	def check_packages(self):
		if sys.argv[1] == 'new':
			system_setup()
