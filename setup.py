############################################################################
#
#  Copyright 2017
#
#   https://github.com/shahzebsiddiqui/buildtest-framework
#
#    This file is part of buildtest.
#
#    buildtest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    buildtest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################


"""
@author: Shahzeb Siddiqui (Pfizer)
"""

from setuptools import setup


setup(name='Tcl-buildtest-config',
      version='0.2.2',
      description="""Tcl tests for buildtest-framework""",
      url='https://github.com/HPC-buildtest/Tcl-buildtest-config',
      author='Shahzeb Siddiqui',
      author_email='shahzebmsiddiqui@gmail.com',
      license='GPLv2',
      platforms = "Linux",
      install_requires=['buildtest-framework==0.2.2'],      
      zip_safe=False)

