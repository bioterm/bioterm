# grafanaApiClient.LegacyAlertsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_by_id**](LegacyAlertsApi.md#get_alert_by_id) | **GET** /alerts/{alert_id} | Get alert by ID.
[**get_alerts**](LegacyAlertsApi.md#get_alerts) | **GET** /alerts | Get legacy alerts.
[**get_dashboard_states**](LegacyAlertsApi.md#get_dashboard_states) | **GET** /alerts/states-for-dashboard | Get alert states for a dashboard.
[**pause_alert**](LegacyAlertsApi.md#pause_alert) | **POST** /alerts/{alert_id}/pause | Pause/unpause alert by id.
[**test_alert**](LegacyAlertsApi.md#test_alert) | **POST** /alerts/test | Test alert.


# **get_alert_by_id**
> LegacyAlert get_alert_by_id(alert_id)

Get alert by ID.

“evalMatches” data in the response is cached in the db when and only when the state of the alert changes (e.g. transitioning from “ok” to “alerting” state). If data from one server triggers the alert first and, before that server is seen leaving alerting state, a second server also enters a state that would trigger the alert, the second server will not be visible in “evalMatches” data.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.legacy_alert import LegacyAlert
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
    api_instance = grafanaApiClient.LegacyAlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 

    try:
        # Get alert by ID.
        api_response = api_instance.get_alert_by_id(alert_id)
        print("The response of LegacyAlertsApi->get_alert_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsApi->get_alert_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 

### Return type

[**LegacyAlert**](LegacyAlert.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> List[AlertListItemDTO] get_alerts(dashboard_id=dashboard_id, panel_id=panel_id, query=query, state=state, limit=limit, folder_id=folder_id, dashboard_query=dashboard_query, dashboard_tag=dashboard_tag)

Get legacy alerts.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_list_item_dto import AlertListItemDTO
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
    api_instance = grafanaApiClient.LegacyAlertsApi(api_client)
    dashboard_id = ['dashboard_id_example'] # List[str] | Limit response to alerts in specified dashboard(s). You can specify multiple dashboards. (optional)
    panel_id = 56 # int | Limit response to alert for a specified panel on a dashboard. (optional)
    query = 'query_example' # str | Limit response to alerts having a name like this value. (optional)
    state = 'state_example' # str | Return alerts with one or more of the following alert states (optional)
    limit = 56 # int | Limit response to X number of alerts. (optional)
    folder_id = ['folder_id_example'] # List[str] | Limit response to alerts of dashboards in specified folder(s). You can specify multiple folders (optional)
    dashboard_query = 'dashboard_query_example' # str | Limit response to alerts having a dashboard name like this value./ Limit response to alerts having a dashboard name like this value. (optional)
    dashboard_tag = ['dashboard_tag_example'] # List[str] | Limit response to alerts of dashboards with specified tags. To do an “AND” filtering with multiple tags, specify the tags parameter multiple times (optional)

    try:
        # Get legacy alerts.
        api_response = api_instance.get_alerts(dashboard_id=dashboard_id, panel_id=panel_id, query=query, state=state, limit=limit, folder_id=folder_id, dashboard_query=dashboard_query, dashboard_tag=dashboard_tag)
        print("The response of LegacyAlertsApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsApi->get_alerts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | [**List[str]**](str.md)| Limit response to alerts in specified dashboard(s). You can specify multiple dashboards. | [optional] 
 **panel_id** | **int**| Limit response to alert for a specified panel on a dashboard. | [optional] 
 **query** | **str**| Limit response to alerts having a name like this value. | [optional] 
 **state** | **str**| Return alerts with one or more of the following alert states | [optional] 
 **limit** | **int**| Limit response to X number of alerts. | [optional] 
 **folder_id** | [**List[str]**](str.md)| Limit response to alerts of dashboards in specified folder(s). You can specify multiple folders | [optional] 
 **dashboard_query** | **str**| Limit response to alerts having a dashboard name like this value./ Limit response to alerts having a dashboard name like this value. | [optional] 
 **dashboard_tag** | [**List[str]**](str.md)| Limit response to alerts of dashboards with specified tags. To do an “AND” filtering with multiple tags, specify the tags parameter multiple times | [optional] 

### Return type

[**List[AlertListItemDTO]**](AlertListItemDTO.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_states**
> List[AlertStateInfoDTO] get_dashboard_states(dashboard_id)

Get alert states for a dashboard.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_state_info_dto import AlertStateInfoDTO
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
    api_instance = grafanaApiClient.LegacyAlertsApi(api_client)
    dashboard_id = 56 # int | 

    try:
        # Get alert states for a dashboard.
        api_response = api_instance.get_dashboard_states(dashboard_id)
        print("The response of LegacyAlertsApi->get_dashboard_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsApi->get_dashboard_states: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**|  | 

### Return type

[**List[AlertStateInfoDTO]**](AlertStateInfoDTO.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_alert**
> PauseAlert200Response pause_alert(alert_id, pause_alert_command)

Pause/unpause alert by id.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.pause_alert200_response import PauseAlert200Response
from grafanaApiClient.models.pause_alert_command import PauseAlertCommand
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
    api_instance = grafanaApiClient.LegacyAlertsApi(api_client)
    alert_id = 'alert_id_example' # str | 
    pause_alert_command = grafanaApiClient.PauseAlertCommand() # PauseAlertCommand | 

    try:
        # Pause/unpause alert by id.
        api_response = api_instance.pause_alert(alert_id, pause_alert_command)
        print("The response of LegacyAlertsApi->pause_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsApi->pause_alert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **pause_alert_command** | [**PauseAlertCommand**](PauseAlertCommand.md)|  | 

### Return type

[**PauseAlert200Response**](PauseAlert200Response.md)

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

# **test_alert**
> AlertTestResult test_alert(alert_test_command=alert_test_command)

Test alert.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_test_command import AlertTestCommand
from grafanaApiClient.models.alert_test_result import AlertTestResult
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
    api_instance = grafanaApiClient.LegacyAlertsApi(api_client)
    alert_test_command = grafanaApiClient.AlertTestCommand() # AlertTestCommand |  (optional)

    try:
        # Test alert.
        api_response = api_instance.test_alert(alert_test_command=alert_test_command)
        print("The response of LegacyAlertsApi->test_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsApi->test_alert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_test_command** | [**AlertTestCommand**](AlertTestCommand.md)|  | [optional] 

### Return type

[**AlertTestResult**](AlertTestResult.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**422** | UnprocessableEntityError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

