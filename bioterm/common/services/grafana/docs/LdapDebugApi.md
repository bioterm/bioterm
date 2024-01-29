# grafanaApiClient.LdapDebugApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sync_status**](LdapDebugApi.md#get_sync_status) | **GET** /admin/ldap-sync-status | Returns the current state of the LDAP background sync integration.


# **get_sync_status**
> ActiveSyncStatusDTO get_sync_status()

Returns the current state of the LDAP background sync integration.

You need to have a permission with action `ldap.status:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.active_sync_status_dto import ActiveSyncStatusDTO
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
    api_instance = grafanaApiClient.LdapDebugApi(api_client)

    try:
        # Returns the current state of the LDAP background sync integration.
        api_response = api_instance.get_sync_status()
        print("The response of LdapDebugApi->get_sync_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapDebugApi->get_sync_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveSyncStatusDTO**](ActiveSyncStatusDTO.md)

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

