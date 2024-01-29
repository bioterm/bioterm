# grafanaApiClient.DatasourcesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_source**](DatasourcesApi.md#add_data_source) | **POST** /datasources | Create a data source.
[**call_datasource_resource_by_id**](DatasourcesApi.md#call_datasource_resource_by_id) | **GET** /datasources/{id}/resources/{datasource_proxy_route} | Fetch data source resources by Id.
[**call_datasource_resource_with_uid**](DatasourcesApi.md#call_datasource_resource_with_uid) | **GET** /datasources/uid/{uid}/resources/{datasource_proxy_route} | Fetch data source resources.
[**check_datasource_health_by_id**](DatasourcesApi.md#check_datasource_health_by_id) | **GET** /datasources/{id}/health | Sends a health check request to the plugin datasource identified by the ID.
[**check_datasource_health_with_uid**](DatasourcesApi.md#check_datasource_health_with_uid) | **GET** /datasources/uid/{uid}/health | Sends a health check request to the plugin datasource identified by the UID.
[**datasource_proxy_delet_ecalls**](DatasourcesApi.md#datasource_proxy_delet_ecalls) | **DELETE** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy DELETE calls.
[**datasource_proxy_deleteby_ui_dcalls**](DatasourcesApi.md#datasource_proxy_deleteby_ui_dcalls) | **DELETE** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy DELETE calls.
[**datasource_proxy_ge_tcalls**](DatasourcesApi.md#datasource_proxy_ge_tcalls) | **GET** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy GET calls.
[**datasource_proxy_getby_ui_dcalls**](DatasourcesApi.md#datasource_proxy_getby_ui_dcalls) | **GET** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy GET calls.
[**datasource_proxy_pos_tcalls**](DatasourcesApi.md#datasource_proxy_pos_tcalls) | **POST** /datasources/proxy/{id}/{datasource_proxy_route} | Data source proxy POST calls.
[**datasource_proxy_postby_ui_dcalls**](DatasourcesApi.md#datasource_proxy_postby_ui_dcalls) | **POST** /datasources/proxy/uid/{uid}/{datasource_proxy_route} | Data source proxy POST calls.
[**delete_data_source_by_id**](DatasourcesApi.md#delete_data_source_by_id) | **DELETE** /datasources/{id} | Delete an existing data source by id.
[**delete_data_source_by_name**](DatasourcesApi.md#delete_data_source_by_name) | **DELETE** /datasources/name/{name} | Delete an existing data source by name.
[**delete_data_source_by_uid**](DatasourcesApi.md#delete_data_source_by_uid) | **DELETE** /datasources/uid/{uid} | Delete an existing data source by UID.
[**get_data_source_by_id**](DatasourcesApi.md#get_data_source_by_id) | **GET** /datasources/{id} | Get a single data source by Id.
[**get_data_source_by_name**](DatasourcesApi.md#get_data_source_by_name) | **GET** /datasources/name/{name} | Get a single data source by Name.
[**get_data_source_by_uid**](DatasourcesApi.md#get_data_source_by_uid) | **GET** /datasources/uid/{uid} | Get a single data source by UID.
[**get_data_source_id_by_name**](DatasourcesApi.md#get_data_source_id_by_name) | **GET** /datasources/id/{name} | Get data source Id by Name.
[**get_data_sources**](DatasourcesApi.md#get_data_sources) | **GET** /datasources | Get all data sources.
[**update_data_source_by_id**](DatasourcesApi.md#update_data_source_by_id) | **PUT** /datasources/{id} | Update an existing data source by its sequential ID.
[**update_data_source_by_uid**](DatasourcesApi.md#update_data_source_by_uid) | **PUT** /datasources/uid/{uid} | Update an existing data source.


# **add_data_source**
> AddDataSource200Response add_data_source(add_data_source_command)

Create a data source.

By defining `password` and `basicAuthPassword` under secureJsonData property Grafana encrypts them securely as an encrypted blob in the database. The response then lists the encrypted fields under secureJsonFields.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:create`

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.add_data_source200_response import AddDataSource200Response
from grafanaApiClient.models.add_data_source_command import AddDataSourceCommand
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    add_data_source_command = grafanaApiClient.AddDataSourceCommand() # AddDataSourceCommand | 

    try:
        # Create a data source.
        api_response = api_instance.add_data_source(add_data_source_command)
        print("The response of DatasourcesApi->add_data_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->add_data_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_data_source_command** | [**AddDataSourceCommand**](AddDataSourceCommand.md)|  | 

### Return type

[**AddDataSource200Response**](AddDataSource200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**409** | ConflictError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_datasource_resource_by_id**
> SuccessResponseBody call_datasource_resource_by_id(datasource_proxy_route, id)

Fetch data source resources by Id.

Please refer to [updated API](#/datasources/callDatasourceResourceWithUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    id = 'id_example' # str | 

    try:
        # Fetch data source resources by Id.
        api_response = api_instance.call_datasource_resource_by_id(datasource_proxy_route, id)
        print("The response of DatasourcesApi->call_datasource_resource_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->call_datasource_resource_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_datasource_resource_with_uid**
> SuccessResponseBody call_datasource_resource_with_uid(datasource_proxy_route, uid)

Fetch data source resources.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    uid = 'uid_example' # str | 

    try:
        # Fetch data source resources.
        api_response = api_instance.call_datasource_resource_with_uid(datasource_proxy_route, uid)
        print("The response of DatasourcesApi->call_datasource_resource_with_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->call_datasource_resource_with_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_datasource_health_by_id**
> SuccessResponseBody check_datasource_health_by_id(id)

Sends a health check request to the plugin datasource identified by the ID.

Please refer to [updated API](#/datasources/checkDatasourceHealthWithUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Sends a health check request to the plugin datasource identified by the ID.
        api_response = api_instance.check_datasource_health_by_id(id)
        print("The response of DatasourcesApi->check_datasource_health_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->check_datasource_health_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_datasource_health_with_uid**
> SuccessResponseBody check_datasource_health_with_uid(uid)

Sends a health check request to the plugin datasource identified by the UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Sends a health check request to the plugin datasource identified by the UID.
        api_response = api_instance.check_datasource_health_with_uid(uid)
        print("The response of DatasourcesApi->check_datasource_health_with_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->check_datasource_health_with_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_delet_ecalls**
> datasource_proxy_delet_ecalls(id, datasource_proxy_route)

Data source proxy DELETE calls.

Proxies all calls to the actual data source.  Please refer to [updated API](#/datasources/datasourceProxyDELETEByUIDcalls) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    id = 'id_example' # str | 
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 

    try:
        # Data source proxy DELETE calls.
        api_instance.datasource_proxy_delet_ecalls(id, datasource_proxy_route)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_delet_ecalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_deleteby_ui_dcalls**
> datasource_proxy_deleteby_ui_dcalls(uid, datasource_proxy_route)

Data source proxy DELETE calls.

Proxies all calls to the actual data source.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    uid = 'uid_example' # str | 
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 

    try:
        # Data source proxy DELETE calls.
        api_instance.datasource_proxy_deleteby_ui_dcalls(uid, datasource_proxy_route)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_deleteby_ui_dcalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **datasource_proxy_route** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_ge_tcalls**
> datasource_proxy_ge_tcalls(datasource_proxy_route, id)

Data source proxy GET calls.

Proxies all calls to the actual data source.  Please refer to [updated API](#/datasources/datasourceProxyGETByUIDcalls) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    id = 'id_example' # str | 

    try:
        # Data source proxy GET calls.
        api_instance.datasource_proxy_ge_tcalls(datasource_proxy_route, id)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_ge_tcalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_getby_ui_dcalls**
> datasource_proxy_getby_ui_dcalls(datasource_proxy_route, uid)

Data source proxy GET calls.

Proxies all calls to the actual data source.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    uid = 'uid_example' # str | 

    try:
        # Data source proxy GET calls.
        api_instance.datasource_proxy_getby_ui_dcalls(datasource_proxy_route, uid)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_getby_ui_dcalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_pos_tcalls**
> datasource_proxy_pos_tcalls(datasource_proxy_route, id, body)

Data source proxy POST calls.

Proxies all calls to the actual data source. The data source should support POST methods for the specific path and role as defined  Please refer to [updated API](#/datasources/datasourceProxyPOSTByUIDcalls) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Data source proxy POST calls.
        api_instance.datasource_proxy_pos_tcalls(datasource_proxy_route, id, body)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_pos_tcalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (empty) |  -  |
**202** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasource_proxy_postby_ui_dcalls**
> datasource_proxy_postby_ui_dcalls(datasource_proxy_route, uid, body)

Data source proxy POST calls.

Proxies all calls to the actual data source. The data source should support POST methods for the specific path and role as defined

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    datasource_proxy_route = 'datasource_proxy_route_example' # str | 
    uid = 'uid_example' # str | 
    body = None # object | 

    try:
        # Data source proxy POST calls.
        api_instance.datasource_proxy_postby_ui_dcalls(datasource_proxy_route, uid, body)
    except Exception as e:
        print("Exception when calling DatasourcesApi->datasource_proxy_postby_ui_dcalls: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_proxy_route** | **str**|  | 
 **uid** | **str**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (empty) |  -  |
**202** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_source_by_id**
> SuccessResponseBody delete_data_source_by_id(id)

Delete an existing data source by id.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/deleteDataSourceByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an existing data source by id.
        api_response = api_instance.delete_data_source_by_id(id)
        print("The response of DatasourcesApi->delete_data_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->delete_data_source_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_source_by_name**
> DeleteDataSourceByName200Response delete_data_source_by_name(name)

Delete an existing data source by name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.delete_data_source_by_name200_response import DeleteDataSourceByName200Response
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete an existing data source by name.
        api_response = api_instance.delete_data_source_by_name(name)
        print("The response of DatasourcesApi->delete_data_source_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->delete_data_source_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**DeleteDataSourceByName200Response**](DeleteDataSourceByName200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_source_by_uid**
> SuccessResponseBody delete_data_source_by_uid(uid)

Delete an existing data source by UID.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:delete` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:kLtEtcRGk` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Delete an existing data source by UID.
        api_response = api_instance.delete_data_source_by_uid(uid)
        print("The response of DatasourcesApi->delete_data_source_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->delete_data_source_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OKResponse is returned if the request was successful. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_by_id**
> DataSource get_data_source_by_id(id)

Get a single data source by Id.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/getDataSourceByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.data_source import DataSource
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a single data source by Id.
        api_response = api_instance.get_data_source_by_id(id)
        print("The response of DatasourcesApi->get_data_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->get_data_source_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_by_name**
> DataSource get_data_source_by_name(name)

Get a single data source by Name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.data_source import DataSource
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get a single data source by Name.
        api_response = api_instance.get_data_source_by_name(name)
        print("The response of DatasourcesApi->get_data_source_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->get_data_source_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_by_uid**
> DataSource get_data_source_by_uid(uid)

Get a single data source by UID.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:kLtEtcRGk` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.data_source import DataSource
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Get a single data source by UID.
        api_response = api_instance.get_data_source_by_uid(uid)
        print("The response of DatasourcesApi->get_data_source_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->get_data_source_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_id_by_name**
> GetDataSourceIdByName200Response get_data_source_id_by_name(name)

Get data source Id by Name.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scopes: `datasources:*`, `datasources:name:*` and `datasources:name:test_datasource` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.get_data_source_id_by_name200_response import GetDataSourceIdByName200Response
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get data source Id by Name.
        api_response = api_instance.get_data_source_id_by_name(name)
        print("The response of DatasourcesApi->get_data_source_id_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->get_data_source_id_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**GetDataSourceIdByName200Response**](GetDataSourceIdByName200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_sources**
> List[DataSourceListItemDTO] get_data_sources()

Get all data sources.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:read` and scope: `datasources:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.data_source_list_item_dto import DataSourceListItemDTO
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)

    try:
        # Get all data sources.
        api_response = api_instance.get_data_sources()
        print("The response of DatasourcesApi->get_data_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->get_data_sources: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DataSourceListItemDTO]**](DataSourceListItemDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_source_by_id**
> AddDataSource200Response update_data_source_by_id(id, update_data_source_command)

Update an existing data source by its sequential ID.

Similar to creating a data source, `password` and `basicAuthPassword` should be defined under secureJsonData in order to be stored securely as an encrypted blob in the database. Then, the encrypted fields are listed under secureJsonFields section in the response.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:write` and scopes: `datasources:*`, `datasources:id:*` and `datasources:id:1` (single data source).  Please refer to [updated API](#/datasources/updateDataSourceByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.add_data_source200_response import AddDataSource200Response
from grafanaApiClient.models.update_data_source_command import UpdateDataSourceCommand
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    id = 'id_example' # str | 
    update_data_source_command = grafanaApiClient.UpdateDataSourceCommand() # UpdateDataSourceCommand | 

    try:
        # Update an existing data source by its sequential ID.
        api_response = api_instance.update_data_source_by_id(id, update_data_source_command)
        print("The response of DatasourcesApi->update_data_source_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->update_data_source_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_data_source_command** | [**UpdateDataSourceCommand**](UpdateDataSourceCommand.md)|  | 

### Return type

[**AddDataSource200Response**](AddDataSource200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_source_by_uid**
> AddDataSource200Response update_data_source_by_uid(uid, update_data_source_command)

Update an existing data source.

Similar to creating a data source, `password` and `basicAuthPassword` should be defined under secureJsonData in order to be stored securely as an encrypted blob in the database. Then, the encrypted fields are listed under secureJsonFields section in the response.  If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:write` and scopes: `datasources:*`, `datasources:uid:*` and `datasources:uid:1` (single data source).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.add_data_source200_response import AddDataSource200Response
from grafanaApiClient.models.update_data_source_command import UpdateDataSourceCommand
from grafanaApiClient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = grafanaApiClient.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.DatasourcesApi(api_client)
    uid = 'uid_example' # str | 
    update_data_source_command = grafanaApiClient.UpdateDataSourceCommand() # UpdateDataSourceCommand | 

    try:
        # Update an existing data source.
        api_response = api_instance.update_data_source_by_uid(uid, update_data_source_command)
        print("The response of DatasourcesApi->update_data_source_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourcesApi->update_data_source_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **update_data_source_command** | [**UpdateDataSourceCommand**](UpdateDataSourceCommand.md)|  | 

### Return type

[**AddDataSource200Response**](AddDataSource200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

