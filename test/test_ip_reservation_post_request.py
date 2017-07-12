# coding: utf-8

"""
    IPReservations

    An IP reservation is the allocation of a public IP address from an IP address pool. After creating an IP reservation, you can associate it with an instance by using an IP association, to enable access between the Internet and the instance.<p>You can add, delete, update, and view IP reservations using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.ip_reservation_post_request import IPReservationPostRequest


class TestIPReservationPostRequest(unittest.TestCase):
    """ IPReservationPostRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIPReservationPostRequest(self):
        """
        Test IPReservationPostRequest
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = swagger_client.models.ip_reservation_post_request.IPReservationPostRequest()
        pass


if __name__ == '__main__':
    unittest.main()
