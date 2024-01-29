# grafanaApiClient.ProvisioningApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**route_delete_alert_rule**](ProvisioningApi.md#route_delete_alert_rule) | **DELETE** /api/v1/provisioning/alert-rules/{UID} | Delete a specific alert rule by UID.
[**route_delete_contactpoints**](ProvisioningApi.md#route_delete_contactpoints) | **DELETE** /api/v1/provisioning/contact-points/{UID} | Delete a contact point.
[**route_delete_mute_timing**](ProvisioningApi.md#route_delete_mute_timing) | **DELETE** /api/v1/provisioning/mute-timings/{name} | Delete a mute timing.
[**route_delete_template**](ProvisioningApi.md#route_delete_template) | **DELETE** /api/v1/provisioning/templates/{name} | Delete a template.
[**route_get_alert_rule**](ProvisioningApi.md#route_get_alert_rule) | **GET** /api/v1/provisioning/alert-rules/{UID} | Get a specific alert rule by UID.
[**route_get_alert_rule_export**](ProvisioningApi.md#route_get_alert_rule_export) | **GET** /api/v1/provisioning/alert-rules/{UID}/export | Export an alert rule in provisioning file format.
[**route_get_alert_rule_group**](ProvisioningApi.md#route_get_alert_rule_group) | **GET** /api/v1/provisioning/folder/{FolderUID}/rule-groups/{Group} | Get a rule group.
[**route_get_alert_rule_group_export**](ProvisioningApi.md#route_get_alert_rule_group_export) | **GET** /api/v1/provisioning/folder/{FolderUID}/rule-groups/{Group}/export | Export an alert rule group in provisioning file format.
[**route_get_alert_rules**](ProvisioningApi.md#route_get_alert_rules) | **GET** /api/v1/provisioning/alert-rules | Get all the alert rules.
[**route_get_alert_rules_export**](ProvisioningApi.md#route_get_alert_rules_export) | **GET** /api/v1/provisioning/alert-rules/export | Export all alert rules in provisioning file format.
[**route_get_contactpoints**](ProvisioningApi.md#route_get_contactpoints) | **GET** /api/v1/provisioning/contact-points | Get all the contact points.
[**route_get_contactpoints_export**](ProvisioningApi.md#route_get_contactpoints_export) | **GET** /api/v1/provisioning/contact-points/export | Export all contact points in provisioning file format.
[**route_get_mute_timing**](ProvisioningApi.md#route_get_mute_timing) | **GET** /api/v1/provisioning/mute-timings/{name} | Get a mute timing.
[**route_get_mute_timings**](ProvisioningApi.md#route_get_mute_timings) | **GET** /api/v1/provisioning/mute-timings | Get all the mute timings.
[**route_get_policy_tree**](ProvisioningApi.md#route_get_policy_tree) | **GET** /api/v1/provisioning/policies | Get the notification policy tree.
[**route_get_policy_tree_export**](ProvisioningApi.md#route_get_policy_tree_export) | **GET** /api/v1/provisioning/policies/export | Export the notification policy tree in provisioning file format.
[**route_get_template**](ProvisioningApi.md#route_get_template) | **GET** /api/v1/provisioning/templates/{name} | Get a notification template.
[**route_get_templates**](ProvisioningApi.md#route_get_templates) | **GET** /api/v1/provisioning/templates | Get all notification templates.
[**route_post_alert_rule**](ProvisioningApi.md#route_post_alert_rule) | **POST** /api/v1/provisioning/alert-rules | Create a new alert rule.
[**route_post_contactpoints**](ProvisioningApi.md#route_post_contactpoints) | **POST** /api/v1/provisioning/contact-points | Create a contact point.
[**route_post_mute_timing**](ProvisioningApi.md#route_post_mute_timing) | **POST** /api/v1/provisioning/mute-timings | Create a new mute timing.
[**route_put_alert_rule**](ProvisioningApi.md#route_put_alert_rule) | **PUT** /api/v1/provisioning/alert-rules/{UID} | Update an existing alert rule.
[**route_put_alert_rule_group**](ProvisioningApi.md#route_put_alert_rule_group) | **PUT** /api/v1/provisioning/folder/{FolderUID}/rule-groups/{Group} | Update the interval of a rule group.
[**route_put_contactpoint**](ProvisioningApi.md#route_put_contactpoint) | **PUT** /api/v1/provisioning/contact-points/{UID} | Update an existing contact point.
[**route_put_mute_timing**](ProvisioningApi.md#route_put_mute_timing) | **PUT** /api/v1/provisioning/mute-timings/{name} | Replace an existing mute timing.
[**route_put_policy_tree**](ProvisioningApi.md#route_put_policy_tree) | **PUT** /api/v1/provisioning/policies | Sets the notification policy tree.
[**route_put_template**](ProvisioningApi.md#route_put_template) | **PUT** /api/v1/provisioning/templates/{name} | Updates an existing notification template.
[**route_reset_policy_tree**](ProvisioningApi.md#route_reset_policy_tree) | **DELETE** /api/v1/provisioning/policies | Clears the notification policy tree.


# **route_delete_alert_rule**
> route_delete_alert_rule(uid)

Delete a specific alert rule by UID.

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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | Alert rule UID

    try:
        # Delete a specific alert rule by UID.
        api_instance.route_delete_alert_rule(uid)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_delete_alert_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alert rule UID | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  The alert rule was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_delete_contactpoints**
> route_delete_contactpoints(uid)

Delete a contact point.

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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | UID is the contact point unique identifier

    try:
        # Delete a contact point.
        api_instance.route_delete_contactpoints(uid)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_delete_contactpoints: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| UID is the contact point unique identifier | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  The contact point was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_delete_mute_timing**
> route_delete_mute_timing(name)

Delete a mute timing.

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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Mute timing name

    try:
        # Delete a mute timing.
        api_instance.route_delete_mute_timing(name)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_delete_mute_timing: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Mute timing name | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  The mute timing was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_delete_template**
> route_delete_template(name)

Delete a template.

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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Template Name

    try:
        # Delete a template.
        api_instance.route_delete_template(name)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_delete_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template Name | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  The template was deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rule**
> ProvisionedAlertRule route_get_alert_rule(uid)

Get a specific alert rule by UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.provisioned_alert_rule import ProvisionedAlertRule
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | Alert rule UID

    try:
        # Get a specific alert rule by UID.
        api_response = api_instance.route_get_alert_rule(uid)
        print("The response of ProvisioningApi->route_get_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alert rule UID | 

### Return type

[**ProvisionedAlertRule**](ProvisionedAlertRule.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProvisionedAlertRule |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rule_export**
> AlertingFileExport route_get_alert_rule_export(uid, download=download, format=format)

Export an alert rule in provisioning file format.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alerting_file_export import AlertingFileExport
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | Alert rule UID
    download = False # bool | Whether to initiate a download of the file or not. (optional) (default to False)
    format = 'yaml' # str | Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. (optional) (default to 'yaml')

    try:
        # Export an alert rule in provisioning file format.
        api_response = api_instance.route_get_alert_rule_export(uid, download=download, format=format)
        print("The response of ProvisioningApi->route_get_alert_rule_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rule_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alert rule UID | 
 **download** | **bool**| Whether to initiate a download of the file or not. | [optional] [default to False]
 **format** | **str**| Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. | [optional] [default to &#39;yaml&#39;]

### Return type

[**AlertingFileExport**](AlertingFileExport.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertingFileExport |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rule_group**
> AlertRuleGroup route_get_alert_rule_group(folder_uid, group)

Get a rule group.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_rule_group import AlertRuleGroup
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    folder_uid = 'folder_uid_example' # str | 
    group = 'group_example' # str | 

    try:
        # Get a rule group.
        api_response = api_instance.route_get_alert_rule_group(folder_uid, group)
        print("The response of ProvisioningApi->route_get_alert_rule_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rule_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
 **group** | **str**|  | 

### Return type

[**AlertRuleGroup**](AlertRuleGroup.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertRuleGroup |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rule_group_export**
> AlertingFileExport route_get_alert_rule_group_export(folder_uid, group, download=download, format=format)

Export an alert rule group in provisioning file format.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alerting_file_export import AlertingFileExport
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    folder_uid = 'folder_uid_example' # str | 
    group = 'group_example' # str | 
    download = False # bool | Whether to initiate a download of the file or not. (optional) (default to False)
    format = 'yaml' # str | Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. (optional) (default to 'yaml')

    try:
        # Export an alert rule group in provisioning file format.
        api_response = api_instance.route_get_alert_rule_group_export(folder_uid, group, download=download, format=format)
        print("The response of ProvisioningApi->route_get_alert_rule_group_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rule_group_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
 **group** | **str**|  | 
 **download** | **bool**| Whether to initiate a download of the file or not. | [optional] [default to False]
 **format** | **str**| Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. | [optional] [default to &#39;yaml&#39;]

### Return type

[**AlertingFileExport**](AlertingFileExport.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, text/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertingFileExport |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rules**
> List[ProvisionedAlertRule] route_get_alert_rules()

Get all the alert rules.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.provisioned_alert_rule import ProvisionedAlertRule
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Get all the alert rules.
        api_response = api_instance.route_get_alert_rules()
        print("The response of ProvisioningApi->route_get_alert_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rules: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ProvisionedAlertRule]**](ProvisionedAlertRule.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProvisionedAlertRules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_alert_rules_export**
> AlertingFileExport route_get_alert_rules_export(download=download, format=format, folder_uid=folder_uid, group=group, rule_uid=rule_uid)

Export all alert rules in provisioning file format.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alerting_file_export import AlertingFileExport
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    download = False # bool | Whether to initiate a download of the file or not. (optional) (default to False)
    format = 'yaml' # str | Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. (optional) (default to 'yaml')
    folder_uid = ['folder_uid_example'] # List[str] | UIDs of folders from which to export rules (optional)
    group = 'group_example' # str | Name of group of rules to export. Must be specified only together with a single folder UID (optional)
    rule_uid = 'rule_uid_example' # str | UID of alert rule to export. If specified, parameters folderUid and group must be empty. (optional)

    try:
        # Export all alert rules in provisioning file format.
        api_response = api_instance.route_get_alert_rules_export(download=download, format=format, folder_uid=folder_uid, group=group, rule_uid=rule_uid)
        print("The response of ProvisioningApi->route_get_alert_rules_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_alert_rules_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download** | **bool**| Whether to initiate a download of the file or not. | [optional] [default to False]
 **format** | **str**| Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. | [optional] [default to &#39;yaml&#39;]
 **folder_uid** | [**List[str]**](str.md)| UIDs of folders from which to export rules | [optional] 
 **group** | **str**| Name of group of rules to export. Must be specified only together with a single folder UID | [optional] 
 **rule_uid** | **str**| UID of alert rule to export. If specified, parameters folderUid and group must be empty. | [optional] 

### Return type

[**AlertingFileExport**](AlertingFileExport.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertingFileExport |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_contactpoints**
> List[EmbeddedContactPoint] route_get_contactpoints(name=name)

Get all the contact points.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.embedded_contact_point import EmbeddedContactPoint
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Filter by name (optional)

    try:
        # Get all the contact points.
        api_response = api_instance.route_get_contactpoints(name=name)
        print("The response of ProvisioningApi->route_get_contactpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_contactpoints: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name | [optional] 

### Return type

[**List[EmbeddedContactPoint]**](EmbeddedContactPoint.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactPoints |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_contactpoints_export**
> AlertingFileExport route_get_contactpoints_export(download=download, format=format, decrypt=decrypt, name=name)

Export all contact points in provisioning file format.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alerting_file_export import AlertingFileExport
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    download = False # bool | Whether to initiate a download of the file or not. (optional) (default to False)
    format = 'yaml' # str | Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. (optional) (default to 'yaml')
    decrypt = False # bool | Whether any contained secure settings should be decrypted or left redacted. Redacted settings will contain RedactedValue instead. Currently, only org admin can view decrypted secure settings. (optional) (default to False)
    name = 'name_example' # str | Filter by name (optional)

    try:
        # Export all contact points in provisioning file format.
        api_response = api_instance.route_get_contactpoints_export(download=download, format=format, decrypt=decrypt, name=name)
        print("The response of ProvisioningApi->route_get_contactpoints_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_contactpoints_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download** | **bool**| Whether to initiate a download of the file or not. | [optional] [default to False]
 **format** | **str**| Format of the downloaded file, either yaml or json. Accept header can also be used, but the query parameter will take precedence. | [optional] [default to &#39;yaml&#39;]
 **decrypt** | **bool**| Whether any contained secure settings should be decrypted or left redacted. Redacted settings will contain RedactedValue instead. Currently, only org admin can view decrypted secure settings. | [optional] [default to False]
 **name** | **str**| Filter by name | [optional] 

### Return type

[**AlertingFileExport**](AlertingFileExport.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertingFileExport |  -  |
**403** | PermissionDenied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_mute_timing**
> MuteTimeInterval route_get_mute_timing(name)

Get a mute timing.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.mute_time_interval import MuteTimeInterval
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Mute timing name

    try:
        # Get a mute timing.
        api_response = api_instance.route_get_mute_timing(name)
        print("The response of ProvisioningApi->route_get_mute_timing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_mute_timing: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Mute timing name | 

### Return type

[**MuteTimeInterval**](MuteTimeInterval.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuteTimeInterval |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_mute_timings**
> List[MuteTimeInterval] route_get_mute_timings()

Get all the mute timings.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.mute_time_interval import MuteTimeInterval
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Get all the mute timings.
        api_response = api_instance.route_get_mute_timings()
        print("The response of ProvisioningApi->route_get_mute_timings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_mute_timings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[MuteTimeInterval]**](MuteTimeInterval.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuteTimings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_policy_tree**
> Route route_get_policy_tree()

Get the notification policy tree.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.route import Route
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Get the notification policy tree.
        api_response = api_instance.route_get_policy_tree()
        print("The response of ProvisioningApi->route_get_policy_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_policy_tree: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Route**](Route.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Route |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_policy_tree_export**
> AlertingFileExport route_get_policy_tree_export()

Export the notification policy tree in provisioning file format.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alerting_file_export import AlertingFileExport
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Export the notification policy tree in provisioning file format.
        api_response = api_instance.route_get_policy_tree_export()
        print("The response of ProvisioningApi->route_get_policy_tree_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_policy_tree_export: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertingFileExport**](AlertingFileExport.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertingFileExport |  -  |
**404** | NotFound |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_template**
> NotificationTemplate route_get_template(name)

Get a notification template.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.notification_template import NotificationTemplate
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Template Name

    try:
        # Get a notification template.
        api_response = api_instance.route_get_template(name)
        print("The response of ProvisioningApi->route_get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template Name | 

### Return type

[**NotificationTemplate**](NotificationTemplate.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NotificationTemplate |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_get_templates**
> List[NotificationTemplate] route_get_templates()

Get all notification templates.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.notification_template import NotificationTemplate
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Get all notification templates.
        api_response = api_instance.route_get_templates()
        print("The response of ProvisioningApi->route_get_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_get_templates: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[NotificationTemplate]**](NotificationTemplate.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NotificationTemplates |  -  |
**404** |  Not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_post_alert_rule**
> ProvisionedAlertRule route_post_alert_rule(x_disable_provenance=x_disable_provenance, provisioned_alert_rule=provisioned_alert_rule)

Create a new alert rule.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.provisioned_alert_rule import ProvisionedAlertRule
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    x_disable_provenance = 'x_disable_provenance_example' # str |  (optional)
    provisioned_alert_rule = grafanaApiClient.ProvisionedAlertRule() # ProvisionedAlertRule |  (optional)

    try:
        # Create a new alert rule.
        api_response = api_instance.route_post_alert_rule(x_disable_provenance=x_disable_provenance, provisioned_alert_rule=provisioned_alert_rule)
        print("The response of ProvisioningApi->route_post_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_post_alert_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_disable_provenance** | **str**|  | [optional] 
 **provisioned_alert_rule** | [**ProvisionedAlertRule**](ProvisionedAlertRule.md)|  | [optional] 

### Return type

[**ProvisionedAlertRule**](ProvisionedAlertRule.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProvisionedAlertRule |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_post_contactpoints**
> EmbeddedContactPoint route_post_contactpoints(embedded_contact_point=embedded_contact_point)

Create a contact point.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.embedded_contact_point import EmbeddedContactPoint
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    embedded_contact_point = grafanaApiClient.EmbeddedContactPoint() # EmbeddedContactPoint |  (optional)

    try:
        # Create a contact point.
        api_response = api_instance.route_post_contactpoints(embedded_contact_point=embedded_contact_point)
        print("The response of ProvisioningApi->route_post_contactpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_post_contactpoints: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedded_contact_point** | [**EmbeddedContactPoint**](EmbeddedContactPoint.md)|  | [optional] 

### Return type

[**EmbeddedContactPoint**](EmbeddedContactPoint.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | EmbeddedContactPoint |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_post_mute_timing**
> MuteTimeInterval route_post_mute_timing(mute_time_interval=mute_time_interval)

Create a new mute timing.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.mute_time_interval import MuteTimeInterval
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    mute_time_interval = grafanaApiClient.MuteTimeInterval() # MuteTimeInterval |  (optional)

    try:
        # Create a new mute timing.
        api_response = api_instance.route_post_mute_timing(mute_time_interval=mute_time_interval)
        print("The response of ProvisioningApi->route_post_mute_timing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_post_mute_timing: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_time_interval** | [**MuteTimeInterval**](MuteTimeInterval.md)|  | [optional] 

### Return type

[**MuteTimeInterval**](MuteTimeInterval.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MuteTimeInterval |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_alert_rule**
> ProvisionedAlertRule route_put_alert_rule(uid, x_disable_provenance=x_disable_provenance, provisioned_alert_rule=provisioned_alert_rule)

Update an existing alert rule.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.provisioned_alert_rule import ProvisionedAlertRule
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | Alert rule UID
    x_disable_provenance = 'x_disable_provenance_example' # str |  (optional)
    provisioned_alert_rule = grafanaApiClient.ProvisionedAlertRule() # ProvisionedAlertRule |  (optional)

    try:
        # Update an existing alert rule.
        api_response = api_instance.route_put_alert_rule(uid, x_disable_provenance=x_disable_provenance, provisioned_alert_rule=provisioned_alert_rule)
        print("The response of ProvisioningApi->route_put_alert_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_alert_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| Alert rule UID | 
 **x_disable_provenance** | **str**|  | [optional] 
 **provisioned_alert_rule** | [**ProvisionedAlertRule**](ProvisionedAlertRule.md)|  | [optional] 

### Return type

[**ProvisionedAlertRule**](ProvisionedAlertRule.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProvisionedAlertRule |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_alert_rule_group**
> AlertRuleGroup route_put_alert_rule_group(folder_uid, group, alert_rule_group=alert_rule_group)

Update the interval of a rule group.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.alert_rule_group import AlertRuleGroup
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    folder_uid = 'folder_uid_example' # str | 
    group = 'group_example' # str | 
    alert_rule_group = grafanaApiClient.AlertRuleGroup() # AlertRuleGroup |  (optional)

    try:
        # Update the interval of a rule group.
        api_response = api_instance.route_put_alert_rule_group(folder_uid, group, alert_rule_group=alert_rule_group)
        print("The response of ProvisioningApi->route_put_alert_rule_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_alert_rule_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_uid** | **str**|  | 
 **group** | **str**|  | 
 **alert_rule_group** | [**AlertRuleGroup**](AlertRuleGroup.md)|  | [optional] 

### Return type

[**AlertRuleGroup**](AlertRuleGroup.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AlertRuleGroup |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_contactpoint**
> object route_put_contactpoint(uid, embedded_contact_point=embedded_contact_point)

Update an existing contact point.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.embedded_contact_point import EmbeddedContactPoint
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    uid = 'uid_example' # str | UID is the contact point unique identifier
    embedded_contact_point = grafanaApiClient.EmbeddedContactPoint() # EmbeddedContactPoint |  (optional)

    try:
        # Update an existing contact point.
        api_response = api_instance.route_put_contactpoint(uid, embedded_contact_point=embedded_contact_point)
        print("The response of ProvisioningApi->route_put_contactpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_contactpoint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| UID is the contact point unique identifier | 
 **embedded_contact_point** | [**EmbeddedContactPoint**](EmbeddedContactPoint.md)|  | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ack |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_mute_timing**
> MuteTimeInterval route_put_mute_timing(name, mute_time_interval=mute_time_interval)

Replace an existing mute timing.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.mute_time_interval import MuteTimeInterval
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Mute timing name
    mute_time_interval = grafanaApiClient.MuteTimeInterval() # MuteTimeInterval |  (optional)

    try:
        # Replace an existing mute timing.
        api_response = api_instance.route_put_mute_timing(name, mute_time_interval=mute_time_interval)
        print("The response of ProvisioningApi->route_put_mute_timing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_mute_timing: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Mute timing name | 
 **mute_time_interval** | [**MuteTimeInterval**](MuteTimeInterval.md)|  | [optional] 

### Return type

[**MuteTimeInterval**](MuteTimeInterval.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuteTimeInterval |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_policy_tree**
> object route_put_policy_tree(route=route)

Sets the notification policy tree.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.route import Route
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    route = grafanaApiClient.Route() # Route | The new notification routing tree to use (optional)

    try:
        # Sets the notification policy tree.
        api_response = api_instance.route_put_policy_tree(route=route)
        print("The response of ProvisioningApi->route_put_policy_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_policy_tree: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route** | [**Route**](Route.md)| The new notification routing tree to use | [optional] 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ack |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_put_template**
> NotificationTemplate route_put_template(name, notification_template_content=notification_template_content)

Updates an existing notification template.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.notification_template import NotificationTemplate
from grafanaApiClient.models.notification_template_content import NotificationTemplateContent
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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)
    name = 'name_example' # str | Template Name
    notification_template_content = grafanaApiClient.NotificationTemplateContent() # NotificationTemplateContent |  (optional)

    try:
        # Updates an existing notification template.
        api_response = api_instance.route_put_template(name, notification_template_content=notification_template_content)
        print("The response of ProvisioningApi->route_put_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_put_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template Name | 
 **notification_template_content** | [**NotificationTemplateContent**](NotificationTemplateContent.md)|  | [optional] 

### Return type

[**NotificationTemplate**](NotificationTemplate.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | NotificationTemplate |  -  |
**400** | ValidationError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_reset_policy_tree**
> object route_reset_policy_tree()

Clears the notification policy tree.

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
    api_instance = grafanaApiClient.ProvisioningApi(api_client)

    try:
        # Clears the notification policy tree.
        api_response = api_instance.route_reset_policy_tree()
        print("The response of ProvisioningApi->route_reset_policy_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvisioningApi->route_reset_policy_tree: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Ack |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

