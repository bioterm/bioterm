# grafanaApiClient.DsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_metrics_with_expressions**](DsApi.md#query_metrics_with_expressions) | **POST** /ds/query | DataSource query metrics with expressions.


# **query_metrics_with_expressions**
> QueryDataResponse query_metrics_with_expressions(metric_request)

DataSource query metrics with expressions.

If you are running Grafana Enterprise and have Fine-grained access control enabled you need to have a permission with action: `datasources:query`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.metric_request import MetricRequest
from grafanaApiClient.models.query_data_response import QueryDataResponse
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
    api_instance = grafanaApiClient.DsApi(api_client)
    metric_request = grafanaApiClient.MetricRequest() # MetricRequest | 

    try:
        # DataSource query metrics with expressions.
        api_response = api_instance.query_metrics_with_expressions(metric_request)
        print("The response of DsApi->query_metrics_with_expressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DsApi->query_metrics_with_expressions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_request** | [**MetricRequest**](MetricRequest.md)|  | 

### Return type

[**QueryDataResponse**](QueryDataResponse.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**207** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

