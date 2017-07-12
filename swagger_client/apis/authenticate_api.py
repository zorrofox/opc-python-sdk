# coding: utf-8

"""
    Authenticate

    A POST request to this resource authenticates the specified user and returns an authentication cookie, which you can specify in subsequent API calls to Oracle Compute Cloud Service.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class AuthenticateApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_authenticate(self, body, **kwargs):
        """
        Authenticate User
        <b>Note:</b> This request returns an authentication token in the <code>Set-Cookie</code> response header. The token expires after 30 minutes. A valid (that is, unexpired) authentication token must be included in every request to the service, in the <code>Cookie</code>: request header. The client making the API call must examine the cookie expiry time and discard it if the cookie has expired. Requests sent with expired cookies will result in an <code>Unauthorized</code> error in the response.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_authenticate(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Authenticate body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = False
        if kwargs.get('async'):
            return self.add_authenticate_with_http_info(body, **kwargs)
        else:
            (data) = self.add_authenticate_with_http_info(body, **kwargs)
            return data

    def add_authenticate_with_http_info(self, body, **kwargs):
        """
        Authenticate User
        <b>Note:</b> This request returns an authentication token in the <code>Set-Cookie</code> response header. The token expires after 30 minutes. A valid (that is, unexpired) authentication token must be included in every request to the service, in the <code>Cookie</code>: request header. The client making the API call must examine the cookie expiry time and discard it if the cookie has expired. Requests sent with expired cookies will result in an <code>Unauthorized</code> error in the response.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_authenticate_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Authenticate body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_authenticate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_authenticate`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/authenticate/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)