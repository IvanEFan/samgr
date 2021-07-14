import os
import re

from setuptools import setup, find_packages
from samgr import constant

# python setup.py sdist bdist_wheel
# python -m twine upload --repository testpypi dist/*
# python -m twine upload dist/*

CLASSIFIERS = [
    # https://pypi.org/classifiers/
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Operating System :: OS Independent'
]

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIRED = [re.match(r'^[A-Za-z.]+', line).group() for line in f.readlines() if not len(line.strip()) == 0]

print('REQUIRED = {}'.format(REQUIRED))

setup(
    name=constant.NAME,
    description=constant.DESCRIPTION,
    version=constant.VERSION,
    author=constant.AUTHOR,
    license="GPL-3.0",
    python_requires=">=3.6",
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=CLASSIFIERS,
    entry_points={
        "console_scripts": [
            "samgr=samgr.__main__:cli",
        ]
    },
)
