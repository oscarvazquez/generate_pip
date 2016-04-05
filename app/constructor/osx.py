import sys
import os
import socket

class osx_setup:
	def __init__(self, project_name):
		self.project_name = project_name
		self.generate_folder()

	def generate_folder(self):
		os.system('mkdir ' + self.project_name)
		os.system('cd ' + self.project_name)
		self.setup_file()
		self.runner_file()
		self.manifest_file()
		os.system('touch ' + self.project_name + '/README.rst')
		self.license()
		os.system('touch LICENSE.txt')
		self.src()

	def license(self):
		os.system('touch LICENSE.txt')
		lic = open('LICENSE.txt', 'w')
		lic.write('The MIT License (MIT)\n \n Copyright (c) 2016 {name}\n \n Permission is hereby granted, free of charge, to any person obtaining a copy\n of this software and associated documentation files (the "Software"), to deal\n in the Software without restriction, including without limitation the rights\n to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n copies of the Software, and to permit persons to whom the Software is\n furnished to do so, subject to the following conditions:\n \n The above copyright notice and this permission notice shall be included in\n all copies or substantial portions of the Software.\n \n THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n THE SOFTWARE.\n'.format(name=socket.gethostname()))
		lic.close()

	def setup_file(self):
		os.system('touch ' + self.project_name + '/setup.py')
		setup = open(self.project_name + '/setup.py', 'w')
		setup.write('import re\nfrom setuptools import setup, find_packages\n\nwith open("README.rst", "rb") as f:\n\tlong_descr = f.read().decode("utf-8")\n\nsetup(\n\tname = "{app_name}",\n\tpackages = find_packages(),\n\tentry_points = {console_script},\n\tversion = version,\n\tdescription = "",\n\tlong_description = long_descr,\n\tauthor = "{name}",\n\tauthor_email = "",\n\turl = ""\n)'.format(location='src/' + self.project_name + '.py', app_name=self.project_name, console_script='{\n \t\t\t"console_scripts": ["' + self.project_name +' = src.'+ self.project_name +':main"]\n\t\t}', name=socket.gethostname()))
		setup.close()

	def manifest_file(self):
		os.system('touch ' + self.project_name + '/MANIFEST.in')
		manifest = open(self.project_name + '/MANIFEST.in', 'w')
		manifest.write('include LICENSE.txt README.rst '+ self.project_name +'-runner.py')
		manifest.write('recursive-exclude *.pyc\n')
		manifest.write('recursive-exclude *.git\n')


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

