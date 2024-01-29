# grafanaApiClient.FolderPermissionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_folder_permission_list**](FolderPermissionsApi.md#get_folder_permission_list) | **GET** /folders/{folder_uid}/permissions | Gets all existing permissions for the folder with the given &#x60;uid&#x60;.
[**update_folder_permissions**](FolderPermissionsApi.md#update_folder_permissions) | **POST** /folders/{folder_uid}/permissions | Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.


# **get_folder_permission_list**
> List[DashboardACLInfoDTO] get_folder_permission_list(folder_uid)

Gets all existing permissions for the folder with the given `uid`.

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
    api_instance = grafanaApiClient.FolderPermissionsApi(api_client)
    folder_uid = 'folder_uid_example' # str | 

    try:
        # Gets all existing permissions for the folder with the given `uid`.
        api_response = api_instance.get_folder_permission_list(folder_uid)
        print("The response of FolderPermissionsApi->get_folder_permission_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderPermissionsApi->get_folder_permission_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 

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

# **update_folder_permissions**
> SuccessResponseBody update_folder_permissions(folder_uid, update_dashboard_acl_command)

Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.

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
    api_instance = grafanaApiClient.FolderPermissionsApi(api_client)
    folder_uid = 'folder_uid_example' # str | 
    update_dashboard_acl_command = grafanaApiClient.UpdateDashboardACLCommand() # UpdateDashboardACLCommand | 

    try:
        # Updates permissions for a folder. This operation will remove existing permissions if they’re not included in the request.
        api_response = api_instance.update_folder_permissions(folder_uid, update_dashboard_acl_command)
        print("The response of FolderPermissionsApi->update_folder_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FolderPermissionsApi->update_folder_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

