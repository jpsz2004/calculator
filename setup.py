from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Juan Pablo Sánchez Zapata',
    author_email='juan.sanchez8@utp.edu.co',
    description='A simple calculator package',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jpsz2004/calculator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
