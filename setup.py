# coding: utf-8

"""
    IPAssociations

    An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.<p>You can create, delete, and view IP associations using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="IPAssociations",
    author_email="",
    url="",
    keywords=["Swagger", "IPAssociations"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.&lt;p&gt;You can create, delete, and view IP associations using the HTTP requests listed below.
    """
)
