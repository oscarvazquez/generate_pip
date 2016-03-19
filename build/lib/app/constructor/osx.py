import sys
import os

class osx_setup:
	def __init__(self, project_name):
		print 'its going into osx setup '
		self.project_name = project_name
		self.generate_folder()

	def generate_folder(self):
		print 'this is where im going to start generating folders'
		os.system('mkdir ' + self.project_name)
		os.system('cd ' + self.project_name)
		self.setup_file()
		self.runner_file()
		os.system('touch ' + self.project_name + '/MANIFEST.in')
		os.system('touch ' + self.project_name + '/README.rst')
		self.src()

	def setup_file(self):
		os.system('touch ' + self.project_name + '/setup.py')
		setup = open(self.project_name + '/setup.py', 'w')
		setup.write('import re\nfrom setuptools import setup, find_packages\n\nwith open("README.rst", "rb") as f:\n\tlong_descr = f.read().decode("utf-8")\n\nsetup(\n\tname = "{app_name}",\n\tpackages = find_packages(),\n\tentry_points = {console_script},\n\tversion = version,\n\tdescription = "",\n\tlong_description = long_descr,\n\tauthor = "",\n\tauthor_email = "",\n\turl = ""\n)'.format(location='src/' + self.project_name + '.py', app_name=self.project_name, console_script='{\n \t\t\t"console_scripts": ["' + self.project_name +' = src.'+ self.project_name +':main"]\n\t\t}'))
		setup.close()

	def runner_file(self):
		os.system('touch ' + self.project_name + '/' + self.project_name + '-runner.py')
		runner = open(self.project_name + '/' + self.project_name + '-runner.py', 'w')
		runner.write('from src.'+ self.project_name +' import main\n\nif __name__ == "__main__":\n\tmain()')
		runner.close()

	def src(self):
		os.system('mkdir ' + self.project_name + '/src')
		os.system('touch ' + self.project_name + '/src/__init__.py')
		os.system('touch ' + self.project_name + '/src/__main__.py')
		main = open(self.project_name + '/src/__main__.py', 'w')
		main.write('from .'+ self.project_name +' import main\nmain()')
		os.system('touch ' + self.project_name + '/src/' + self.project_name + '.py')
		main_code = open(self.project_name + '/src/' + self.project_name + '.py', 'w')
		main_code.write('import sys\n\nclass main:\n\tdef __init__(self):\n\t\tprint "this is where you are going to write your code!"\n\t\t# This is going to house all of the users inputs when\n\t\t# calling this funciton from the command line\n\t\tprint sys.argv\n\t\tself.start_coding()\n\tdef start_coding(self):\n\t\tprint "Start Coding!"\n')
		main_code.close()

