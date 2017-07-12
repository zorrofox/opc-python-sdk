# swagger-client
An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.<p>You can create, delete, and view IP associations using the HTTP requests listed below.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
body = swagger_client.IPAssociationPostRequest() # IPAssociationPostRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try:
    # Create an IP Association
    api_response = api_instance.add_ip_association(body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->add_ip_association: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IPAssociationsApi* | [**add_ip_association**](docs/IPAssociationsApi.md#add_ip_association) | **POST** /ip/association/ | Create an IP Association
*IPAssociationsApi* | [**delete_ip_association**](docs/IPAssociationsApi.md#delete_ip_association) | **DELETE** /ip/association/{name} | Delete an IP Association
*IPAssociationsApi* | [**discover_ip_association**](docs/IPAssociationsApi.md#discover_ip_association) | **GET** /ip/association/{container} | Retrieve Names of all IP Associations and Subcontainers in a Container
*IPAssociationsApi* | [**discover_root_ip_association**](docs/IPAssociationsApi.md#discover_root_ip_association) | **GET** /ip/association/ | Retrieve Names of Containers
*IPAssociationsApi* | [**get_ip_association**](docs/IPAssociationsApi.md#get_ip_association) | **GET** /ip/association/{name} | Retrieve Details of an IP Association
*IPAssociationsApi* | [**list_ip_association**](docs/IPAssociationsApi.md#list_ip_association) | **GET** /ip/association/{container}/ | Retrieve Details of all IP Associations in a Container


## Documentation For Models

 - [IPAssociationDiscoverResponse](docs/IPAssociationDiscoverResponse.md)
 - [IPAssociationListResponse](docs/IPAssociationListResponse.md)
 - [IPAssociationPostRequest](docs/IPAssociationPostRequest.md)
 - [IPAssociationResponse](docs/IPAssociationResponse.md)
 - [Interval](docs/Interval.md)
 - [DailyWeeklyInterval](docs/DailyWeeklyInterval.md)
 - [HourlyInterval](docs/HourlyInterval.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



