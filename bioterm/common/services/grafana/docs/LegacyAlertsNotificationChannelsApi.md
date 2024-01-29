# grafanaApiClient.LegacyAlertsNotificationChannelsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#create_alert_notification_channel) | **POST** /alert-notifications | Create notification channel.
[**delete_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#delete_alert_notification_channel) | **DELETE** /alert-notifications/{notification_channel_id} | Delete alert notification by ID.
[**delete_alert_notification_channel_by_uid**](LegacyAlertsNotificationChannelsApi.md#delete_alert_notification_channel_by_uid) | **DELETE** /alert-notifications/uid/{notification_channel_uid} | Delete alert notification by UID.
[**get_alert_notification_channel_by_id**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channel_by_id) | **GET** /alert-notifications/{notification_channel_id} | Get notification channel by ID.
[**get_alert_notification_channel_by_uid**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channel_by_uid) | **GET** /alert-notifications/uid/{notification_channel_uid} | Get notification channel by UID.
[**get_alert_notification_channels**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_channels) | **GET** /alert-notifications | Get all notification channels.
[**get_alert_notification_lookup**](LegacyAlertsNotificationChannelsApi.md#get_alert_notification_lookup) | **GET** /alert-notifications/lookup | Get all notification channels (lookup).
[**notification_channel_test**](LegacyAlertsNotificationChannelsApi.md#notification_channel_test) | **POST** /alert-notifications/test | Test notification channel.
[**update_alert_notification_channel**](LegacyAlertsNotificationChannelsApi.md#update_alert_notification_channel) | **PUT** /alert-notifications/{notification_channel_id} | Update notification channel by ID.
[**update_alert_notification_channel_by_uid**](LegacyAlertsNotificationChannelsApi.md#update_alert_notification_channel_by_uid) | **PUT** /alert-notifications/uid/{notification_channel_uid} | Update notification channel by UID.


# **create_alert_notification_channel**
> AlertNotification create_alert_notification_channel(create_alert_notification_command)

Create notification channel.

You can find the full list of [supported notifiers](https://grafana.com/docs/grafana/latest/alerting/old-alerting/notifications/#list-of-supported-notifiers) on the alert notifiers page.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
from grafanaApiClient.models.create_alert_notification_command import CreateAlertNotificationCommand
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    create_alert_notification_command = grafanaApiClient.CreateAlertNotificationCommand() # CreateAlertNotificationCommand | 

    try:
        # Create notification channel.
        api_response = api_instance.create_alert_notification_channel(create_alert_notification_command)
        print("The response of LegacyAlertsNotificationChannelsApi->create_alert_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->create_alert_notification_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_notification_command** | [**CreateAlertNotificationCommand**](CreateAlertNotificationCommand.md)|  | 

### Return type

[**AlertNotification**](AlertNotification.md)

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

# **delete_alert_notification_channel**
> SuccessResponseBody delete_alert_notification_channel(notification_channel_id)

Delete alert notification by ID.

Deletes an existing notification channel identified by ID.

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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | 

    try:
        # Delete alert notification by ID.
        api_response = api_instance.delete_alert_notification_channel(notification_channel_id)
        print("The response of LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 

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

# **delete_alert_notification_channel_by_uid**
> DeleteAlertNotificationChannelByUID200Response delete_alert_notification_channel_by_uid(notification_channel_uid)

Delete alert notification by UID.

Deletes an existing notification channel identified by UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.delete_alert_notification_channel_by_uid200_response import DeleteAlertNotificationChannelByUID200Response
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_uid = 'notification_channel_uid_example' # str | 

    try:
        # Delete alert notification by UID.
        api_response = api_instance.delete_alert_notification_channel_by_uid(notification_channel_uid)
        print("The response of LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->delete_alert_notification_channel_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 

### Return type

[**DeleteAlertNotificationChannelByUID200Response**](DeleteAlertNotificationChannelByUID200Response.md)

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

# **get_alert_notification_channel_by_id**
> AlertNotification get_alert_notification_channel_by_id(notification_channel_id)

Get notification channel by ID.

Returns the notification channel given the notification channel ID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | 

    try:
        # Get notification channel by ID.
        api_response = api_instance.get_alert_notification_channel_by_id(notification_channel_id)
        print("The response of LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 

### Return type

[**AlertNotification**](AlertNotification.md)

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

# **get_alert_notification_channel_by_uid**
> AlertNotification get_alert_notification_channel_by_uid(notification_channel_uid)

Get notification channel by UID.

Returns the notification channel given the notification channel UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_uid = 'notification_channel_uid_example' # str | 

    try:
        # Get notification channel by UID.
        api_response = api_instance.get_alert_notification_channel_by_uid(notification_channel_uid)
        print("The response of LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channel_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 

### Return type

[**AlertNotification**](AlertNotification.md)

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

# **get_alert_notification_channels**
> List[AlertNotification] get_alert_notification_channels()

Get all notification channels.

Returns all notification channels that the authenticated user has permission to view.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)

    try:
        # Get all notification channels.
        api_response = api_instance.get_alert_notification_channels()
        print("The response of LegacyAlertsNotificationChannelsApi->get_alert_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_channels: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AlertNotification]**](AlertNotification.md)

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

# **get_alert_notification_lookup**
> List[AlertNotificationLookup] get_alert_notification_lookup()

Get all notification channels (lookup).

Returns all notification channels, but with less detailed information. Accessible by any authenticated user and is mainly used by providing alert notification channels in Grafana UI when configuring alert rule.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification_lookup import AlertNotificationLookup
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)

    try:
        # Get all notification channels (lookup).
        api_response = api_instance.get_alert_notification_lookup()
        print("The response of LegacyAlertsNotificationChannelsApi->get_alert_notification_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->get_alert_notification_lookup: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AlertNotificationLookup]**](AlertNotificationLookup.md)

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

# **notification_channel_test**
> SuccessResponseBody notification_channel_test(notification_test_command)

Test notification channel.

Sends a test notification to the channel.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.notification_test_command import NotificationTestCommand
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_test_command = grafanaApiClient.NotificationTestCommand() # NotificationTestCommand | 

    try:
        # Test notification channel.
        api_response = api_instance.notification_channel_test(notification_test_command)
        print("The response of LegacyAlertsNotificationChannelsApi->notification_channel_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->notification_channel_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_test_command** | [**NotificationTestCommand**](NotificationTestCommand.md)|  | 

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
**412** | (empty) |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_notification_channel**
> AlertNotification update_alert_notification_channel(notification_channel_id, update_alert_notification_command)

Update notification channel by ID.

Updates an existing notification channel identified by ID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
from grafanaApiClient.models.update_alert_notification_command import UpdateAlertNotificationCommand
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_id = 56 # int | 
    update_alert_notification_command = grafanaApiClient.UpdateAlertNotificationCommand() # UpdateAlertNotificationCommand | 

    try:
        # Update notification channel by ID.
        api_response = api_instance.update_alert_notification_channel(notification_channel_id, update_alert_notification_command)
        print("The response of LegacyAlertsNotificationChannelsApi->update_alert_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->update_alert_notification_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_id** | **int**|  | 
 **update_alert_notification_command** | [**UpdateAlertNotificationCommand**](UpdateAlertNotificationCommand.md)|  | 

### Return type

[**AlertNotification**](AlertNotification.md)

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

# **update_alert_notification_channel_by_uid**
> AlertNotification update_alert_notification_channel_by_uid(notification_channel_uid, update_alert_notification_with_uid_command)

Update notification channel by UID.

Updates an existing notification channel identified by uid.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_notification import AlertNotification
from grafanaApiClient.models.update_alert_notification_with_uid_command import UpdateAlertNotificationWithUidCommand
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
    api_instance = grafanaApiClient.LegacyAlertsNotificationChannelsApi(api_client)
    notification_channel_uid = 'notification_channel_uid_example' # str | 
    update_alert_notification_with_uid_command = grafanaApiClient.UpdateAlertNotificationWithUidCommand() # UpdateAlertNotificationWithUidCommand | 

    try:
        # Update notification channel by UID.
        api_response = api_instance.update_alert_notification_channel_by_uid(notification_channel_uid, update_alert_notification_with_uid_command)
        print("The response of LegacyAlertsNotificationChannelsApi->update_alert_notification_channel_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyAlertsNotificationChannelsApi->update_alert_notification_channel_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_channel_uid** | **str**|  | 
 **update_alert_notification_with_uid_command** | [**UpdateAlertNotificationWithUidCommand**](UpdateAlertNotificationWithUidCommand.md)|  | 

### Return type

[**AlertNotification**](AlertNotification.md)

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

