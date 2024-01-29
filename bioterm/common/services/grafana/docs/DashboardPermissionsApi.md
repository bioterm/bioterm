# grafanaApiClient.DashboardPermissionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboard_permissions_list_by_id**](DashboardPermissionsApi.md#get_dashboard_permissions_list_by_id) | **GET** /dashboards/id/{DashboardID}/permissions | Gets all existing permissions for the given dashboard.
[**get_dashboard_permissions_list_by_uid**](DashboardPermissionsApi.md#get_dashboard_permissions_list_by_uid) | **GET** /dashboards/uid/{uid}/permissions | Gets all existing permissions for the given dashboard.
[**update_dashboard_permissions_by_id**](DashboardPermissionsApi.md#update_dashboard_permissions_by_id) | **POST** /dashboards/id/{DashboardID}/permissions | Updates permissions for a dashboard.
[**update_dashboard_permissions_by_uid**](DashboardPermissionsApi.md#update_dashboard_permissions_by_uid) | **POST** /dashboards/uid/{uid}/permissions | Updates permissions for a dashboard.


# **get_dashboard_permissions_list_by_id**
> List[DashboardACLInfoDTO] get_dashboard_permissions_list_by_id(dashboard_id)

Gets all existing permissions for the given dashboard.

Please refer to [updated API](#/dashboard_permissions/getDashboardPermissionsListByUID) instead

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_acl_info_dto import DashboardACLInfoDTO
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
    api_instance = grafanaApiClient.DashboardPermissionsApi(api_client)
    dashboard_id = 56 # int | 

    try:
        # Gets all existing permissions for the given dashboard.
        api_response = api_instance.get_dashboard_permissions_list_by_id(dashboard_id)
        print("The response of DashboardPermissionsApi->get_dashboard_permissions_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPermissionsApi->get_dashboard_permissions_list_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

[**List[DashboardACLInfoDTO]**](DashboardACLInfoDTO.md)

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

# **get_dashboard_permissions_list_by_uid**
> List[DashboardACLInfoDTO] get_dashboard_permissions_list_by_uid(uid)

Gets all existing permissions for the given dashboard.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_acl_info_dto import DashboardACLInfoDTO
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
    api_instance = grafanaApiClient.DashboardPermissionsApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Gets all existing permissions for the given dashboard.
        api_response = api_instance.get_dashboard_permissions_list_by_uid(uid)
        print("The response of DashboardPermissionsApi->get_dashboard_permissions_list_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPermissionsApi->get_dashboard_permissions_list_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**List[DashboardACLInfoDTO]**](DashboardACLInfoDTO.md)

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

# **update_dashboard_permissions_by_id**
> SuccessResponseBody update_dashboard_permissions_by_id(dashboard_id, update_dashboard_acl_command)

Updates permissions for a dashboard.

Please refer to [updated API](#/dashboard_permissions/updateDashboardPermissionsByUID) instead  This operation will remove existing permissions if they’re not included in the request.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.models.update_dashboard_acl_command import UpdateDashboardACLCommand
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
    api_instance = grafanaApiClient.DashboardPermissionsApi(api_client)
    dashboard_id = 56 # int | 
    update_dashboard_acl_command = grafanaApiClient.UpdateDashboardACLCommand() # UpdateDashboardACLCommand | 

    try:
        # Updates permissions for a dashboard.
        api_response = api_instance.update_dashboard_permissions_by_id(dashboard_id, update_dashboard_acl_command)
        print("The response of DashboardPermissionsApi->update_dashboard_permissions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPermissionsApi->update_dashboard_permissions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 
 **update_dashboard_acl_command** | [**UpdateDashboardACLCommand**](UpdateDashboardACLCommand.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
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

# **update_dashboard_permissions_by_uid**
> SuccessResponseBody update_dashboard_permissions_by_uid(uid, update_dashboard_acl_command)

Updates permissions for a dashboard.

This operation will remove existing permissions if they’re not included in the request.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.models.update_dashboard_acl_command import UpdateDashboardACLCommand
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
    api_instance = grafanaApiClient.DashboardPermissionsApi(api_client)
    uid = 'uid_example' # str | 
    update_dashboard_acl_command = grafanaApiClient.UpdateDashboardACLCommand() # UpdateDashboardACLCommand | 

    try:
        # Updates permissions for a dashboard.
        api_response = api_instance.update_dashboard_permissions_by_uid(uid, update_dashboard_acl_command)
        print("The response of DashboardPermissionsApi->update_dashboard_permissions_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPermissionsApi->update_dashboard_permissions_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **update_dashboard_acl_command** | [**UpdateDashboardACLCommand**](UpdateDashboardACLCommand.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
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

