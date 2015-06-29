# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1.0'

long_description = (read('../../readme.rst'))

setup(name='nexiles.gateway.example',
      version=version,
      description="A example nexiles|gateway service",
      long_description=long_description,
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='Stefan Eletzhofer',
      author_email='se@nexiles.de',
      url='https://github.com/nexiles/nexiles.gateway.example',
      license='proprietary',
      packages=find_packages('.', exclude=['ez_setup']),
      package_dir={'': '.'},
      package_data={"nexiles.gateway.example": ["templates/*"]},
      namespace_packages=['nexiles', 'nexiles.gateway'],
      include_package_data=True,
      zip_safe=True,
      install_requires=['setuptools',
                        # 'nexiles.tools>=1.5.0'
                        ],
      )
