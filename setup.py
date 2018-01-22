
#!/usr/bin/python

# Copyright 2018 Altran
# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
# Copyright 2011 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if sys.version_info < (2, 7):
    requirements.append('argparse')
elif sys.version_info < (2, 7):
    raise 'Must use python 2.7 or greater'

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='EPEPIN API Server',
    version='1.0',
    author='Asgard Team',
    author_email='',
    description='Ericcson Cucumber Templates API Server',
    long_description=long_description,    
    install_requires=requirements,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    data_files=[('epepin_api/config', ['epepin_api/config/epepin_server.cfg'])],
    license='Apache License 2.0',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: System"
        "Framework :: Flask"
    ],
    entry_points={
        'console_scripts': [
            'epepin=epepin_api.server:main',
        ],
    },

)
