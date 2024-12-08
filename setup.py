from setuptools import setup, find_packages

setup(
	name='project3',
	version='1.0',
	author='Sharvani Gouni',
	author_email='sharvanigouni@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs', 'resources')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)