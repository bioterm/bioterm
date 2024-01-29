# grafanaApiClient.CorrelationsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_correlation**](CorrelationsApi.md#create_correlation) | **POST** /datasources/uid/{sourceUID}/correlations | Add correlation.
[**delete_correlation**](CorrelationsApi.md#delete_correlation) | **DELETE** /datasources/uid/{uid}/correlations/{correlationUID} | Delete a correlation.
[**get_correlation**](CorrelationsApi.md#get_correlation) | **GET** /datasources/uid/{sourceUID}/correlations/{correlationUID} | Gets a correlation.
[**get_correlations**](CorrelationsApi.md#get_correlations) | **GET** /datasources/correlations | Gets all correlations.
[**get_correlations_by_source_uid**](CorrelationsApi.md#get_correlations_by_source_uid) | **GET** /datasources/uid/{sourceUID}/correlations | Gets all correlations originating from the given data source.
[**update_correlation**](CorrelationsApi.md#update_correlation) | **PATCH** /datasources/uid/{sourceUID}/correlations/{correlationUID} | Updates a correlation.


# **create_correlation**
> CreateCorrelationResponseBody create_correlation(source_uid, create_correlation_command)

Add correlation.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.create_correlation_command import CreateCorrelationCommand
from grafanaApiClient.models.create_correlation_response_body import CreateCorrelationResponseBody
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    source_uid = 'source_uid_example' # str | 
    create_correlation_command = grafanaApiClient.CreateCorrelationCommand() # CreateCorrelationCommand | 

    try:
        # Add correlation.
        api_response = api_instance.create_correlation(source_uid, create_correlation_command)
        print("The response of CorrelationsApi->create_correlation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->create_correlation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uid** | **str**|  | 
 **create_correlation_command** | [**CreateCorrelationCommand**](CreateCorrelationCommand.md)|  | 

### Return type

[**CreateCorrelationResponseBody**](CreateCorrelationResponseBody.md)

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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_correlation**
> DeleteCorrelationResponseBody delete_correlation(uid, correlation_uid)

Delete a correlation.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.delete_correlation_response_body import DeleteCorrelationResponseBody
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    uid = 'uid_example' # str | 
    correlation_uid = 'correlation_uid_example' # str | 

    try:
        # Delete a correlation.
        api_response = api_instance.delete_correlation(uid, correlation_uid)
        print("The response of CorrelationsApi->delete_correlation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->delete_correlation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 
 **correlation_uid** | **str**|  | 

### Return type

[**DeleteCorrelationResponseBody**](DeleteCorrelationResponseBody.md)

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

# **get_correlation**
> Correlation get_correlation(source_uid, correlation_uid)

Gets a correlation.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.correlation import Correlation
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    source_uid = 'source_uid_example' # str | 
    correlation_uid = 'correlation_uid_example' # str | 

    try:
        # Gets a correlation.
        api_response = api_instance.get_correlation(source_uid, correlation_uid)
        print("The response of CorrelationsApi->get_correlation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->get_correlation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uid** | **str**|  | 
 **correlation_uid** | **str**|  | 

### Return type

[**Correlation**](Correlation.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_correlations**
> List[Correlation] get_correlations(limit=limit, page=page, source_uid=source_uid)

Gets all correlations.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.correlation import Correlation
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    limit = 100 # int | Limit the maximum number of correlations to return per page (optional) (default to 100)
    page = 1 # int | Page index for starting fetching correlations (optional) (default to 1)
    source_uid = ['source_uid_example'] # List[str] | Source datasource UID filter to be applied to correlations (optional)

    try:
        # Gets all correlations.
        api_response = api_instance.get_correlations(limit=limit, page=page, source_uid=source_uid)
        print("The response of CorrelationsApi->get_correlations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->get_correlations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the maximum number of correlations to return per page | [optional] [default to 100]
 **page** | **int**| Page index for starting fetching correlations | [optional] [default to 1]
 **source_uid** | [**List[str]**](str.md)| Source datasource UID filter to be applied to correlations | [optional] 

### Return type

[**List[Correlation]**](Correlation.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_correlations_by_source_uid**
> List[Correlation] get_correlations_by_source_uid(source_uid)

Gets all correlations originating from the given data source.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.correlation import Correlation
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    source_uid = 'source_uid_example' # str | 

    try:
        # Gets all correlations originating from the given data source.
        api_response = api_instance.get_correlations_by_source_uid(source_uid)
        print("The response of CorrelationsApi->get_correlations_by_source_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->get_correlations_by_source_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uid** | **str**|  | 

### Return type

[**List[Correlation]**](Correlation.md)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_correlation**
> UpdateCorrelationResponseBody update_correlation(source_uid, correlation_uid, update_correlation_command=update_correlation_command)

Updates a correlation.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.update_correlation_command import UpdateCorrelationCommand
from grafanaApiClient.models.update_correlation_response_body import UpdateCorrelationResponseBody
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
    api_instance = grafanaApiClient.CorrelationsApi(api_client)
    source_uid = 'source_uid_example' # str | 
    correlation_uid = 'correlation_uid_example' # str | 
    update_correlation_command = grafanaApiClient.UpdateCorrelationCommand() # UpdateCorrelationCommand |  (optional)

    try:
        # Updates a correlation.
        api_response = api_instance.update_correlation(source_uid, correlation_uid, update_correlation_command=update_correlation_command)
        print("The response of CorrelationsApi->update_correlation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrelationsApi->update_correlation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_uid** | **str**|  | 
 **correlation_uid** | **str**|  | 
 **update_correlation_command** | [**UpdateCorrelationCommand**](UpdateCorrelationCommand.md)|  | [optional] 

### Return type

[**UpdateCorrelationResponseBody**](UpdateCorrelationResponseBody.md)

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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

