# -*- coding: utf-8 -*-

#    Copyright 2016 Mirantis, Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

PROJECT = 'jim'

VERSION = '0.1'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'name': 'jim',
    'version': '0.1',

    'author': 'Mirantis',
    'author_email': 'infra@mirantis.com',

    'description': 'Update jenkins configuration using YAML',

    'url': 'https://github.com/fuel-infra/jim',

    'download_url': 'https://github.com/fuel-infra/jim',

    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
     ],

    'platforms': ['Unix'],

    'scripts': [],

    'provides': [],

    'license': ['Apache License 2.0'],

    'install_requires': [
        'click',
        'functools32',
        'jsonschema',
        'MarkupSafe',
        'pyaml',
        'PyYAML',
        'wheel'
    ],

    'packages': find_packages(),
    'include_package_data': True,
    'package_data': {
        'lib': ['schema.yaml'],
        'plugins': ['credentials/resources/*',
                    'gerrit/resources/*',
                    'gearman/resources/*',
                    'jenkins_configuration/resources/*',
                    'throttle/resources/*'],
    },
    'py_modules': ['jim'],
    'entry_points': {
        'console_scripts': [
            'jim = jim:cli',
        ],
    },


    'zip_safe': False,
}

setup(**config)