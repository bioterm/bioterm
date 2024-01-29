# grafanaApiClient.QueryHistoryApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query**](QueryHistoryApi.md#create_query) | **POST** /query-history | Add query to query history.
[**delete_query**](QueryHistoryApi.md#delete_query) | **DELETE** /query-history/{query_history_uid} | Delete query in query history.
[**patch_query_comment**](QueryHistoryApi.md#patch_query_comment) | **PATCH** /query-history/{query_history_uid} | Update comment for query in query history.
[**search_queries**](QueryHistoryApi.md#search_queries) | **GET** /query-history | Query history search.
[**star_query**](QueryHistoryApi.md#star_query) | **POST** /query-history/star/{query_history_uid} | Add star to query in query history.
[**unstar_query**](QueryHistoryApi.md#unstar_query) | **DELETE** /query-history/star/{query_history_uid} | Remove star to query in query history.


# **create_query**
> QueryHistoryResponse create_query(create_query_in_query_history_command)

Add query to query history.

Adds new query to query history.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.create_query_in_query_history_command import CreateQueryInQueryHistoryCommand
from grafanaApiClient.models.query_history_response import QueryHistoryResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    create_query_in_query_history_command = grafanaApiClient.CreateQueryInQueryHistoryCommand() # CreateQueryInQueryHistoryCommand | 

    try:
        # Add query to query history.
        api_response = api_instance.create_query(create_query_in_query_history_command)
        print("The response of QueryHistoryApi->create_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->create_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_query_in_query_history_command** | [**CreateQueryInQueryHistoryCommand**](CreateQueryInQueryHistoryCommand.md)|  | 

### Return type

[**QueryHistoryResponse**](QueryHistoryResponse.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query**
> QueryHistoryDeleteQueryResponse delete_query(query_history_uid)

Delete query in query history.

Deletes an existing query in query history as specified by the UID. This operation cannot be reverted.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.query_history_delete_query_response import QueryHistoryDeleteQueryResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    query_history_uid = 'query_history_uid_example' # str | 

    try:
        # Delete query in query history.
        api_response = api_instance.delete_query(query_history_uid)
        print("The response of QueryHistoryApi->delete_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->delete_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_history_uid** | **str**|  | 

### Return type

[**QueryHistoryDeleteQueryResponse**](QueryHistoryDeleteQueryResponse.md)

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

# **patch_query_comment**
> QueryHistoryResponse patch_query_comment(query_history_uid, patch_query_comment_in_query_history_command)

Update comment for query in query history.

Updates comment for query in query history as specified by the UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.patch_query_comment_in_query_history_command import PatchQueryCommentInQueryHistoryCommand
from grafanaApiClient.models.query_history_response import QueryHistoryResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    query_history_uid = 'query_history_uid_example' # str | 
    patch_query_comment_in_query_history_command = grafanaApiClient.PatchQueryCommentInQueryHistoryCommand() # PatchQueryCommentInQueryHistoryCommand | 

    try:
        # Update comment for query in query history.
        api_response = api_instance.patch_query_comment(query_history_uid, patch_query_comment_in_query_history_command)
        print("The response of QueryHistoryApi->patch_query_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->patch_query_comment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_history_uid** | **str**|  | 
 **patch_query_comment_in_query_history_command** | [**PatchQueryCommentInQueryHistoryCommand**](PatchQueryCommentInQueryHistoryCommand.md)|  | 

### Return type

[**QueryHistoryResponse**](QueryHistoryResponse.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_queries**
> QueryHistorySearchResponse search_queries(datasource_uid=datasource_uid, search_string=search_string, only_starred=only_starred, sort=sort, page=page, limit=limit, var_from=var_from, to=to)

Query history search.

Returns a list of queries in the query history that matches the search criteria. Query history search supports pagination. Use the `limit` parameter to control the maximum number of queries returned; the default limit is 100. You can also use the `page` query parameter to fetch queries from any page other than the first one.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.query_history_search_response import QueryHistorySearchResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    datasource_uid = ['datasource_uid_example'] # List[str] | List of data source UIDs to search for (optional)
    search_string = 'search_string_example' # str | Text inside query or comments that is searched for (optional)
    only_starred = True # bool | Flag indicating if only starred queries should be returned (optional)
    sort = 'time-desc' # str | Sort method (optional) (default to 'time-desc')
    page = 56 # int | Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. (optional)
    limit = 56 # int | Limit the number of returned results (optional)
    var_from = 56 # int | From range for the query history search (optional)
    to = 56 # int | To range for the query history search (optional)

    try:
        # Query history search.
        api_response = api_instance.search_queries(datasource_uid=datasource_uid, search_string=search_string, only_starred=only_starred, sort=sort, page=page, limit=limit, var_from=var_from, to=to)
        print("The response of QueryHistoryApi->search_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->search_queries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasource_uid** | [**List[str]**](str.md)| List of data source UIDs to search for | [optional] 
 **search_string** | **str**| Text inside query or comments that is searched for | [optional] 
 **only_starred** | **bool**| Flag indicating if only starred queries should be returned | [optional] 
 **sort** | **str**| Sort method | [optional] [default to &#39;time-desc&#39;]
 **page** | **int**| Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. | [optional] 
 **limit** | **int**| Limit the number of returned results | [optional] 
 **var_from** | **int**| From range for the query history search | [optional] 
 **to** | **int**| To range for the query history search | [optional] 

### Return type

[**QueryHistorySearchResponse**](QueryHistorySearchResponse.md)

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

# **star_query**
> QueryHistoryResponse star_query(query_history_uid)

Add star to query in query history.

Adds star to query in query history as specified by the UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.query_history_response import QueryHistoryResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    query_history_uid = 'query_history_uid_example' # str | 

    try:
        # Add star to query in query history.
        api_response = api_instance.star_query(query_history_uid)
        print("The response of QueryHistoryApi->star_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->star_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_history_uid** | **str**|  | 

### Return type

[**QueryHistoryResponse**](QueryHistoryResponse.md)

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

# **unstar_query**
> QueryHistoryResponse unstar_query(query_history_uid)

Remove star to query in query history.

Removes star from query in query history as specified by the UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.query_history_response import QueryHistoryResponse
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
    api_instance = grafanaApiClient.QueryHistoryApi(api_client)
    query_history_uid = 'query_history_uid_example' # str | 

    try:
        # Remove star to query in query history.
        api_response = api_instance.unstar_query(query_history_uid)
        print("The response of QueryHistoryApi->unstar_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryHistoryApi->unstar_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_history_uid** | **str**|  | 

### Return type

[**QueryHistoryResponse**](QueryHistoryResponse.md)

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

