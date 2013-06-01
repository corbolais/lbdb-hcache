#!/usr/bin/env python
"""
script to install pwman3
"""

from distutils.core import setup

setup(name="lbdb-hcache",
      version="0.0.1",
      description="lbdb tools for extracting addresses from the mutt header cache",
      author="Ivan Kelly",
      author_email="ivan@ivankelly.net",
      url="http://www.github.com/ivankelly/lbdb-hcache",
      license="GNU GPL",
      scripts=['lbdb-hcache-extract-addresses','lbdb-hcache-search'],
      data_files=[('share/lbdb-hcache/lbdb_modules', ['m_hcache'])]
      )
