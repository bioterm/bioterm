# grafanaApiClient.DashboardVersionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_version_by_id**](DashboardVersionsApi.md#get_dashboard_version_by_id) | **GET** /dashboards/id/{DashboardID}/versions/{DashboardVersionID} | Get a specific dashboard version.
[**get_dashboard_version_by_uid**](DashboardVersionsApi.md#get_dashboard_version_by_uid) | **GET** /dashboards/uid/{uid}/versions/{DashboardVersionID} | Get a specific dashboard version using UID.
[**get_dashboard_versions_by_id**](DashboardVersionsApi.md#get_dashboard_versions_by_id) | **GET** /dashboards/id/{DashboardID}/versions | Gets all existing versions for the dashboard.
[**get_dashboard_versions_by_uid**](DashboardVersionsApi.md#get_dashboard_versions_by_uid) | **GET** /dashboards/uid/{uid}/versions | Gets all existing versions for the dashboard using UID.
[**restore_dashboard_version_by_id**](DashboardVersionsApi.md#restore_dashboard_version_by_id) | **POST** /dashboards/id/{DashboardID}/restore | Restore a dashboard to a given dashboard version.
[**restore_dashboard_version_by_uid**](DashboardVersionsApi.md#restore_dashboard_version_by_uid) | **POST** /dashboards/uid/{uid}/restore | Restore a dashboard to a given dashboard version using UID.


# **get_dashboard_version_by_id**
> DashboardVersionMeta get_dashboard_version_by_id(dashboard_id, dashboard_version_id)

Get a specific dashboard version.

Please refer to [updated API](#/dashboard_versions/getDashboardVersionByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_version_meta import DashboardVersionMeta
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    dashboard_id = 56 # int | 
    dashboard_version_id = 56 # int | 

    try:
        # Get a specific dashboard version.
        api_response = api_instance.get_dashboard_version_by_id(dashboard_id, dashboard_version_id)
        print("The response of DashboardVersionsApi->get_dashboard_version_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->get_dashboard_version_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **dashboard_version_id** | **int**|  | 

### Return type

[**DashboardVersionMeta**](DashboardVersionMeta.md)

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

# **get_dashboard_version_by_uid**
> DashboardVersionMeta get_dashboard_version_by_uid(dashboard_version_id, uid)

Get a specific dashboard version using UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_version_meta import DashboardVersionMeta
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    dashboard_version_id = 56 # int | 
    uid = 'uid_example' # str | 

    try:
        # Get a specific dashboard version using UID.
        api_response = api_instance.get_dashboard_version_by_uid(dashboard_version_id, uid)
        print("The response of DashboardVersionsApi->get_dashboard_version_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->get_dashboard_version_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_version_id** | **int**|  | 
 **uid** | **str**|  | 

### Return type

[**DashboardVersionMeta**](DashboardVersionMeta.md)

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

# **get_dashboard_versions_by_id**
> List[DashboardVersionMeta] get_dashboard_versions_by_id(dashboard_id)

Gets all existing versions for the dashboard.

Please refer to [updated API](#/dashboard_versions/getDashboardVersionsByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_version_meta import DashboardVersionMeta
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    dashboard_id = 56 # int | 

    try:
        # Gets all existing versions for the dashboard.
        api_response = api_instance.get_dashboard_versions_by_id(dashboard_id)
        print("The response of DashboardVersionsApi->get_dashboard_versions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->get_dashboard_versions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

[**List[DashboardVersionMeta]**](DashboardVersionMeta.md)

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

# **get_dashboard_versions_by_uid**
> List[DashboardVersionMeta] get_dashboard_versions_by_uid(uid, limit=limit, start=start)

Gets all existing versions for the dashboard using UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_version_meta import DashboardVersionMeta
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    uid = 'uid_example' # str | 
    limit = 0 # int | Maximum number of results to return (optional) (default to 0)
    start = 0 # int | Version to start from when returning queries (optional) (default to 0)

    try:
        # Gets all existing versions for the dashboard using UID.
        api_response = api_instance.get_dashboard_versions_by_uid(uid, limit=limit, start=start)
        print("The response of DashboardVersionsApi->get_dashboard_versions_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->get_dashboard_versions_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **limit** | **int**| Maximum number of results to return | [optional] [default to 0]
 **start** | **int**| Version to start from when returning queries | [optional] [default to 0]

### Return type

[**List[DashboardVersionMeta]**](DashboardVersionMeta.md)

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

# **restore_dashboard_version_by_id**
> PostDashboard200Response restore_dashboard_version_by_id(dashboard_id, restore_dashboard_version_command)

Restore a dashboard to a given dashboard version.

Please refer to [updated API](#/dashboard_versions/restoreDashboardVersionByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.post_dashboard200_response import PostDashboard200Response
from grafanaApiClient.models.restore_dashboard_version_command import RestoreDashboardVersionCommand
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    dashboard_id = 56 # int | 
    restore_dashboard_version_command = grafanaApiClient.RestoreDashboardVersionCommand() # RestoreDashboardVersionCommand | 

    try:
        # Restore a dashboard to a given dashboard version.
        api_response = api_instance.restore_dashboard_version_by_id(dashboard_id, restore_dashboard_version_command)
        print("The response of DashboardVersionsApi->restore_dashboard_version_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->restore_dashboard_version_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **restore_dashboard_version_command** | [**RestoreDashboardVersionCommand**](RestoreDashboardVersionCommand.md)|  | 

### Return type

[**PostDashboard200Response**](PostDashboard200Response.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dashboard_version_by_uid**
> PostDashboard200Response restore_dashboard_version_by_uid(uid, restore_dashboard_version_command)

Restore a dashboard to a given dashboard version using UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.post_dashboard200_response import PostDashboard200Response
from grafanaApiClient.models.restore_dashboard_version_command import RestoreDashboardVersionCommand
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
    api_instance = grafanaApiClient.DashboardVersionsApi(api_client)
    uid = 'uid_example' # str | 
    restore_dashboard_version_command = grafanaApiClient.RestoreDashboardVersionCommand() # RestoreDashboardVersionCommand | 

    try:
        # Restore a dashboard to a given dashboard version using UID.
        api_response = api_instance.restore_dashboard_version_by_uid(uid, restore_dashboard_version_command)
        print("The response of DashboardVersionsApi->restore_dashboard_version_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardVersionsApi->restore_dashboard_version_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **restore_dashboard_version_command** | [**RestoreDashboardVersionCommand**](RestoreDashboardVersionCommand.md)|  | 

### Return type

[**PostDashboard200Response**](PostDashboard200Response.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

