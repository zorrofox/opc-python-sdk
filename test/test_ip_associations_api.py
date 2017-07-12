# coding: utf-8

"""
    IPAssociations

    An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.<p>You can create, delete, and view IP associations using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.ip_associations_api import IPAssociationsApi


class TestIPAssociationsApi(unittest.TestCase):
    """ IPAssociationsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.ip_associations_api.IPAssociationsApi()

    def tearDown(self):
        pass

    def test_add_ip_association(self):
        """
        Test case for add_ip_association

        Create an IP Association
        """
        pass

    def test_delete_ip_association(self):
        """
        Test case for delete_ip_association

        Delete an IP Association
        """
        pass

    def test_discover_ip_association(self):
        """
        Test case for discover_ip_association

        Retrieve Names of all IP Associations and Subcontainers in a Container
        """
        pass

    def test_discover_root_ip_association(self):
        """
        Test case for discover_root_ip_association

        Retrieve Names of Containers
        """
        pass

    def test_get_ip_association(self):
        """
        Test case for get_ip_association

        Retrieve Details of an IP Association
        """
        pass

    def test_list_ip_association(self):
        """
        Test case for list_ip_association

        Retrieve Details of all IP Associations in a Container
        """
        pass


if __name__ == '__main__':
    unittest.main()
