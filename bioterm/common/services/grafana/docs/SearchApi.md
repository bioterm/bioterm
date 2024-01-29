# grafanaApiClient.SearchApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_sort_options**](SearchApi.md#list_sort_options) | **GET** /search/sorting | List search sorting options.
[**search**](SearchApi.md#search) | **GET** /search | 


# **list_sort_options**
> ListSortOptions200Response list_sort_options()

List search sorting options.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.list_sort_options200_response import ListSortOptions200Response
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
    api_instance = grafanaApiClient.SearchApi(api_client)

    try:
        # List search sorting options.
        api_response = api_instance.list_sort_options()
        print("The response of SearchApi->list_sort_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->list_sort_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSortOptions200Response**](ListSortOptions200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> List[Hit] search(query=query, tag=tag, type=type, dashboard_ids=dashboard_ids, dashboard_uids=dashboard_uids, folder_ids=folder_ids, folder_uids=folder_uids, starred=starred, limit=limit, page=page, permission=permission, sort=sort)



### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.hit import Hit
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
    api_instance = grafanaApiClient.SearchApi(api_client)
    query = 'query_example' # str | Search Query (optional)
    tag = ['tag_example'] # List[str] | List of tags to search for (optional)
    type = 'type_example' # str | Type to search for, dash-folder or dash-db (optional)
    dashboard_ids = [56] # List[int] | List of dashboard id’s to search for This is deprecated: users should use the `dashboardUIDs` query parameter instead (optional)
    dashboard_uids = ['dashboard_uids_example'] # List[str] | List of dashboard uid’s to search for (optional)
    folder_ids = [56] # List[int] | List of folder id’s to search in for dashboards If it's `0` then it will query for the top level folders This is deprecated: users should use the `folderUIDs` query parameter instead (optional)
    folder_uids = ['folder_uids_example'] # List[str] | List of folder UID’s to search in for dashboards If it's an empty string then it will query for the top level folders (optional)
    starred = True # bool | Flag indicating if only starred Dashboards should be returned (optional)
    limit = 56 # int | Limit the number of returned results (max 5000) (optional)
    page = 56 # int | Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. Only available in Grafana v6.2+. (optional)
    permission = 'View' # str | Set to `Edit` to return dashboards/folders that the user can edit (optional) (default to 'View')
    sort = 'alpha-asc' # str | Sort method; for listing all the possible sort methods use the search sorting endpoint. (optional) (default to 'alpha-asc')

    try:
        api_response = api_instance.search(query=query, tag=tag, type=type, dashboard_ids=dashboard_ids, dashboard_uids=dashboard_uids, folder_ids=folder_ids, folder_uids=folder_uids, starred=starred, limit=limit, page=page, permission=permission, sort=sort)
        print("The response of SearchApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search Query | [optional] 
 **tag** | [**List[str]**](str.md)| List of tags to search for | [optional] 
 **type** | **str**| Type to search for, dash-folder or dash-db | [optional] 
 **dashboard_ids** | [**List[int]**](int.md)| List of dashboard id’s to search for This is deprecated: users should use the &#x60;dashboardUIDs&#x60; query parameter instead | [optional] 
 **dashboard_uids** | [**List[str]**](str.md)| List of dashboard uid’s to search for | [optional] 
 **folder_ids** | [**List[int]**](int.md)| List of folder id’s to search in for dashboards If it&#39;s &#x60;0&#x60; then it will query for the top level folders This is deprecated: users should use the &#x60;folderUIDs&#x60; query parameter instead | [optional] 
 **folder_uids** | [**List[str]**](str.md)| List of folder UID’s to search in for dashboards If it&#39;s an empty string then it will query for the top level folders | [optional] 
 **starred** | **bool**| Flag indicating if only starred Dashboards should be returned | [optional] 
 **limit** | **int**| Limit the number of returned results (max 5000) | [optional] 
 **page** | **int**| Use this parameter to access hits beyond limit. Numbering starts at 1. limit param acts as page size. Only available in Grafana v6.2+. | [optional] 
 **permission** | **str**| Set to &#x60;Edit&#x60; to return dashboards/folders that the user can edit | [optional] [default to &#39;View&#39;]
 **sort** | **str**| Sort method; for listing all the possible sort methods use the search sorting endpoint. | [optional] [default to &#39;alpha-asc&#39;]

### Return type

[**List[Hit]**](Hit.md)

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
**422** | UnprocessableEntityError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

