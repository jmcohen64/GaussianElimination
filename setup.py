# setup.py
from setuptools import setup, Extension

# Define the extension module
module = Extension('foo', sources=['foo.c'])

# Call the setup function
setup(
    name='foo',
    version='1.0',
    description='A simple C extension for Python',
    ext_modules=[module],
)
