# coding: utf-8

"""
    IPAssociations

    An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.<p>You can create, delete, and view IP associations using the HTTP requests listed below.

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


class IPAssociationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_ip_association(self, body, **kwargs):
        """
        Create an IP Association
        Creates an association between an IP address and the vcable ID of an instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_ip_association(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param IPAssociationPostRequest body: (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_ip_association_with_http_info(body, **kwargs)
        else:
            (data) = self.add_ip_association_with_http_info(body, **kwargs)
            return data

    def add_ip_association_with_http_info(self, body, **kwargs):
        """
        Create an IP Association
        Creates an association between an IP address and the vcable ID of an instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_ip_association_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param IPAssociationPostRequest body: (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_ip_association" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_ip_association`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

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

        return self.api_client.call_api('/ip/association/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='IPAssociationResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_ip_association(self, name, **kwargs):
        """
        Delete an IP Association
        Deletes the specified IP association. Use this HTTP request when you want to change the public IP address of an instance or if you no longer need a public IP address for the instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_ip_association(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>). (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_ip_association_with_http_info(name, **kwargs)
        else:
            (data) = self.delete_ip_association_with_http_info(name, **kwargs)
            return data

    def delete_ip_association_with_http_info(self, name, **kwargs):
        """
        Delete an IP Association
        Deletes the specified IP association. Use this HTTP request when you want to change the public IP address of an instance or if you no longer need a public IP address for the instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_ip_association_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>). (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ip_association" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_ip_association`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ip/association/{name}', 'DELETE',
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

    def discover_ip_association(self, container, **kwargs):
        """
        Retrieve Names of all IP Associations and Subcontainers in a Container
        Retrieves the names of objects and subcontainers that you can access in the specified container.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.discover_ip_association(container, async=True)
        >>> result = thread.get()

        :param async bool
        :param str container: Specify <code>/Compute-<i>identityDomain</i>/<i>user</i>/</code> to retrieve the names of objects that you can access. Specify <code>/Compute-<i>identityDomain</i>/</code> to retrieve the names of containers that contain objects that you can access. (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationDiscoverResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.discover_ip_association_with_http_info(container, **kwargs)
        else:
            (data) = self.discover_ip_association_with_http_info(container, **kwargs)
            return data

    def discover_ip_association_with_http_info(self, container, **kwargs):
        """
        Retrieve Names of all IP Associations and Subcontainers in a Container
        Retrieves the names of objects and subcontainers that you can access in the specified container.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.discover_ip_association_with_http_info(container, async=True)
        >>> result = thread.get()

        :param async bool
        :param str container: Specify <code>/Compute-<i>identityDomain</i>/<i>user</i>/</code> to retrieve the names of objects that you can access. Specify <code>/Compute-<i>identityDomain</i>/</code> to retrieve the names of containers that contain objects that you can access. (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationDiscoverResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container', 'cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method discover_ip_association" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container' is set
        if ('container' not in params) or (params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `discover_ip_association`")


        collection_formats = {}

        path_params = {}
        if 'container' in params:
            path_params['container'] = params['container']

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+directory+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ip/association/{container}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='IPAssociationDiscoverResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def discover_root_ip_association(self, **kwargs):
        """
        Retrieve Names of Containers
        Retrieves the names of containers that contain objects that you can access. You can use this information to construct the multipart name of an object.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.discover_root_ip_association(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationDiscoverResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.discover_root_ip_association_with_http_info(**kwargs)
        else:
            (data) = self.discover_root_ip_association_with_http_info(**kwargs)
            return data

    def discover_root_ip_association_with_http_info(self, **kwargs):
        """
        Retrieve Names of Containers
        Retrieves the names of containers that contain objects that you can access. You can use this information to construct the multipart name of an object.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.discover_root_ip_association_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationDiscoverResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method discover_root_ip_association" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+directory+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ip/association/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='IPAssociationDiscoverResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_ip_association(self, name, **kwargs):
        """
        Retrieve Details of an IP Association
        <b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_ip_association(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>). (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_ip_association_with_http_info(name, **kwargs)
        else:
            (data) = self.get_ip_association_with_http_info(name, **kwargs)
            return data

    def get_ip_association_with_http_info(self, name, **kwargs):
        """
        Retrieve Details of an IP Association
        <b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_ip_association_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>). (required)
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_association" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_ip_association`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ip/association/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='IPAssociationResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_ip_association(self, container, **kwargs):
        """
        Retrieve Details of all IP Associations in a Container
        Retrieves details of the IP associations that are available in the specified container and match the specified query criteria. If you don't specify any query criteria, then details of all the IP associations in the container are displayed. To filter the search results, you can pass one or more of the following query parameters, by appending them to the URI in the following syntax:<p><code>?parameter1=value1&ampparameter2=value2&ampparameterN=valueN</code><p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_ip_association(container, async=True)
        >>> result = thread.get()

        :param async bool
        :param str container: <code>/Compute-<em>identity_domain</em>/<em>user</em></code> or <p><code>/Compute-<em>identity_domain</em></code> (required)
        :param str parentpool: Use this option if you want to retrieve details of temporary IP addresses from the pool. Specify <code>ippool:/oracle/public/ippool</code> as the value.
        :param str reservation: Use this option if you want to retrieve details of a specific persistent IP address. Specify the name of the reservation in the format, <code>ipreservation:<em>ipreservation_name</em></code>, where <code><em>ipreservation_name</em></code> is three-part name of an existing IP reservation in the <code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code> format.
        :param str vcable: vcable ID of the instance that you want to associate with the IP reservation.<p>For more information about the vcable of an instance, see <a class=\"xref\" href=\"op-instance-{name}-get.html\">Retrieve Details of an Instance</a>.
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_ip_association_with_http_info(container, **kwargs)
        else:
            (data) = self.list_ip_association_with_http_info(container, **kwargs)
            return data

    def list_ip_association_with_http_info(self, container, **kwargs):
        """
        Retrieve Details of all IP Associations in a Container
        Retrieves details of the IP associations that are available in the specified container and match the specified query criteria. If you don't specify any query criteria, then details of all the IP associations in the container are displayed. To filter the search results, you can pass one or more of the following query parameters, by appending them to the URI in the following syntax:<p><code>?parameter1=value1&ampparameter2=value2&ampparameterN=valueN</code><p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_ip_association_with_http_info(container, async=True)
        >>> result = thread.get()

        :param async bool
        :param str container: <code>/Compute-<em>identity_domain</em>/<em>user</em></code> or <p><code>/Compute-<em>identity_domain</em></code> (required)
        :param str parentpool: Use this option if you want to retrieve details of temporary IP addresses from the pool. Specify <code>ippool:/oracle/public/ippool</code> as the value.
        :param str reservation: Use this option if you want to retrieve details of a specific persistent IP address. Specify the name of the reservation in the format, <code>ipreservation:<em>ipreservation_name</em></code>, where <code><em>ipreservation_name</em></code> is three-part name of an existing IP reservation in the <code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code> format.
        :param str vcable: vcable ID of the instance that you want to associate with the IP reservation.<p>For more information about the vcable of an instance, see <a class=\"xref\" href=\"op-instance-{name}-get.html\">Retrieve Details of an Instance</a>.
        :param str cookie: The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call.
        :return: IPAssociationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container', 'parentpool', 'reservation', 'vcable', 'cookie']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ip_association" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container' is set
        if ('container' not in params) or (params['container'] is None):
            raise ValueError("Missing the required parameter `container` when calling `list_ip_association`")


        collection_formats = {}

        path_params = {}
        if 'container' in params:
            path_params['container'] = params['container']

        query_params = []
        if 'parentpool' in params:
            query_params.append(('parentpool', params['parentpool']))
        if 'reservation' in params:
            query_params.append(('reservation', params['reservation']))
        if 'vcable' in params:
            query_params.append(('vcable', params['vcable']))

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/oracle-compute-v3+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/oracle-compute-v3+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ip/association/{container}/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='IPAssociationListResponse',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
