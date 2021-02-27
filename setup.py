from setuptools import (setup, find_packages)

VERSION = '0.2.0'


setup(
    name='na-common',
    version=VERSION,
    url='https://github.com/NewAcropolis/na-common',
    license='MIT',
    author='Ken Tsang',
    description='Shared code for use between New Acropolis apps',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=1.0.2',
    ]
)
