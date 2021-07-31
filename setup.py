import setuptools

with open('readme.md','r') as file:
	long_description=file.read()

setuptools.setup(name='clean_saurabh',
version='0.0.1',
author_name='Saurabh Yadav',
author_email='saurabhyad007@gmail.com',
description='Basic Cleaning',
long_description=long_description,
long_description_content_type='text/markdown',
packages=setuptools.find_packages(),
python_requires='>=3.6',
classifiers=['Programming Language::Python::3',
'License::OSI Approved ::MIT License',
'Operating System ::OS Independent']) #this name should be globally unique

