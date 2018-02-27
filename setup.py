#!/usr/bin/env python3

# Copyright (c) 2018, Stadt Karlsruhe (www.karlsruhe.de)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages
import os.path
import re


HERE = os.path.abspath(os.path.dirname(__file__))
INIT_PY = os.path.join(HERE, 'matomo_api', '__init__.py')
REQUIREMENTS_TXT = os.path.join(HERE, 'requirements.txt')

# Extract version
version = None
with open(INIT_PY, encoding='utf-8') as f:
    for line in f:
        m = re.match(r'__version__\s*=\s*[\'"](.*)[\'"]', line)
        if m:
            version = m.groups()[0]
            break
if version is None:
    raise RuntimeError('Could not extract version from "{}".'.format(INIT_PY))

with open(REQUIREMENTS_TXT, encoding='utf8') as f:
    requirements = f.readlines()


setup(
    name='matomo_api',
    version=version,
    description='Wrapper around the Matomo (formerly Piwik) API',
    long_description='',
    url='https://github.com/stadt-karlsruhe/matomo_api',
    author='Stadt Karlsruhe',
    author_email='transparenz@karlsruhe.de',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='matomo piwik api'.split(),
    packages=find_packages(),
    install_requires=requirements,
)

