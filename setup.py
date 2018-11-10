#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name = 'pyNaomi',
      version = '1.0',
      description = 'Python tools for NAOMI',
#      package_dir = {'':'lib'},
#      packages = find_packages('lib'),
      scripts = ['scripts/modal_disturbance.py',
		 'scripts/fitsview.py'])
