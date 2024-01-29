# grafanaApiClient.SamlApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata**](SamlApi.md#get_metadata) | **GET** /saml/metadata | It exposes the SP (Grafana&#39;s) metadata for the IdP&#39;s consumption.
[**get_saml_logout**](SamlApi.md#get_saml_logout) | **GET** /logout/saml | GetLogout initiates single logout process.
[**get_slo**](SamlApi.md#get_slo) | **GET** /saml/slo | It performs Single Logout (SLO) callback.
[**post_acs**](SamlApi.md#post_acs) | **POST** /saml/acs | It performs Assertion Consumer Service (ACS).
[**post_slo**](SamlApi.md#post_slo) | **POST** /saml/slo | It performs Single Logout (SLO) callback.


# **get_metadata**
> List[int] get_metadata()

It exposes the SP (Grafana's) metadata for the IdP's consumption.

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
    api_instance = grafanaApiClient.SamlApi(api_client)

    try:
        # It exposes the SP (Grafana's) metadata for the IdP's consumption.
        api_response = api_instance.get_metadata()
        print("The response of SamlApi->get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SamlApi->get_metadata: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[int]**

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_logout**
> get_saml_logout()

GetLogout initiates single logout process.

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
    api_instance = grafanaApiClient.SamlApi(api_client)

    try:
        # GetLogout initiates single logout process.
        api_instance.get_saml_logout()
    except Exception as e:
        print("Exception when calling SamlApi->get_saml_logout: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**302** | (empty) |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slo**
> get_slo()

It performs Single Logout (SLO) callback.

There might be two possible requests: 1. Logout response (callback) when Grafana initiates single logout and IdP returns response to logout request. 2. Logout request when another SP initiates single logout and IdP sends logout request to the Grafana, or in case of IdP-initiated logout.

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
    api_instance = grafanaApiClient.SamlApi(api_client)

    try:
        # It performs Single Logout (SLO) callback.
        api_instance.get_slo()
    except Exception as e:
        print("Exception when calling SamlApi->get_slo: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**302** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_acs**
> post_acs(relay_state=relay_state)

It performs Assertion Consumer Service (ACS).

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
    api_instance = grafanaApiClient.SamlApi(api_client)
    relay_state = 'relay_state_example' # str |  (optional)

    try:
        # It performs Assertion Consumer Service (ACS).
        api_instance.post_acs(relay_state=relay_state)
    except Exception as e:
        print("Exception when calling SamlApi->post_acs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relay_state** | **str**|  | [optional] 

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
**302** | (empty) |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_slo**
> post_slo(saml_request=saml_request, saml_response=saml_response)

It performs Single Logout (SLO) callback.

There might be two possible requests: 1. Logout response (callback) when Grafana initiates single logout and IdP returns response to logout request. 2. Logout request when another SP initiates single logout and IdP sends logout request to the Grafana, or in case of IdP-initiated logout.

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
    api_instance = grafanaApiClient.SamlApi(api_client)
    saml_request = 'saml_request_example' # str |  (optional)
    saml_response = 'saml_response_example' # str |  (optional)

    try:
        # It performs Single Logout (SLO) callback.
        api_instance.post_slo(saml_request=saml_request, saml_response=saml_response)
    except Exception as e:
        print("Exception when calling SamlApi->post_slo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_request** | **str**|  | [optional] 
 **saml_response** | **str**|  | [optional] 

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
**302** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

