from sys import platform as _platform
from osx import osx_setup
import sys

class system: 
	def __init__(self):
		if len(sys.argv) > 2:
			self.project_name = sys.argv[2]
			self.check_system()
		else: 
			print 'Add the name of your pip module'

	def check_system(self):
		if _platform == "linux" or _platform == "linux2":
			print 'linux: I haven\'t set this up yet sorry'
		elif _platform == "darwin":
			osx_setup(self.project_name)
		elif _platform == "win32":
			print 'windows: I haven\'t set this up yet sorry'