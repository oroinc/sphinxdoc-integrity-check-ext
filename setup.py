# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__),
                       'requirements.txt'), 'r') as f:
    requirements = f.read()

long_desc = '''
This extension allows to control content of rst document.
It can be useful to verify that examples in documentation with literalinclude of the files from code are still valid.
'''

setup(
    name='oro-sphinx-integrity-check',
    version='0.0.1',
    url='https://github.com/aivus/oro-sphinxdoc-integrity-check-ext',
    license='MIT',
    author='Oro Inc.',
    author_email='iantypenko@oroinc.com',
    description='Sphinx extension to control content of rst document',
    long_description=long_desc,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Sphinx :: Extension',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    dependency_links=[],
    namespace_packages=['sphinxcontrib'],
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
)
