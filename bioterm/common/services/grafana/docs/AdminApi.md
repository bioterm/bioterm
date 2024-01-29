# grafanaApiClient.AdminApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_get_settings**](AdminApi.md#admin_get_settings) | **GET** /admin/settings | Fetch settings.
[**admin_get_stats**](AdminApi.md#admin_get_stats) | **GET** /admin/stats | Fetch Grafana Stats.
[**pause_all_alerts**](AdminApi.md#pause_all_alerts) | **POST** /admin/pause-all-alerts | Pause/unpause all (legacy) alerts.


# **admin_get_settings**
> Dict[str, Dict[str, str]] admin_get_settings()

Fetch settings.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `settings:read` and scopes: `settings:*`, `settings:auth.saml:` and `settings:auth.saml:enabled` (property level).

### Example

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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminApi(api_client)

    try:
        # Fetch settings.
        api_response = api_instance.admin_get_settings()
        print("The response of AdminApi->admin_get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_get_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, Dict[str, str]]**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_stats**
> AdminStats admin_get_stats()

Fetch Grafana Stats.

Only works with Basic Authentication (username and password). See introduction for an explanation. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `server:stats:read`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.admin_stats import AdminStats
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
    api_instance = grafanaApiClient.AdminApi(api_client)

    try:
        # Fetch Grafana Stats.
        api_response = api_instance.admin_get_stats()
        print("The response of AdminApi->admin_get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_get_stats: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminStats**](AdminStats.md)

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

# **pause_all_alerts**
> PauseAllAlerts200Response pause_all_alerts(pause_all_alerts_command)

Pause/unpause all (legacy) alerts.

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.pause_all_alerts200_response import PauseAllAlerts200Response
from grafanaApiClient.models.pause_all_alerts_command import PauseAllAlertsCommand
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminApi(api_client)
    pause_all_alerts_command = grafanaApiClient.PauseAllAlertsCommand() # PauseAllAlertsCommand | 

    try:
        # Pause/unpause all (legacy) alerts.
        api_response = api_instance.pause_all_alerts(pause_all_alerts_command)
        print("The response of AdminApi->pause_all_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->pause_all_alerts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pause_all_alerts_command** | [**PauseAllAlertsCommand**](PauseAllAlertsCommand.md)|  | 

### Return type

[**PauseAllAlerts200Response**](PauseAllAlerts200Response.md)

### Authorization

[basic](../README.md#basic)

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

