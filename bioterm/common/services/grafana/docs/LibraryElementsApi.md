# grafanaApiClient.LibraryElementsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_library_element**](LibraryElementsApi.md#create_library_element) | **POST** /library-elements | Create library element.
[**delete_library_element_by_uid**](LibraryElementsApi.md#delete_library_element_by_uid) | **DELETE** /library-elements/{library_element_uid} | Delete library element.
[**get_library_element_by_name**](LibraryElementsApi.md#get_library_element_by_name) | **GET** /library-elements/name/{library_element_name} | Get library element by name.
[**get_library_element_by_uid**](LibraryElementsApi.md#get_library_element_by_uid) | **GET** /library-elements/{library_element_uid} | Get library element by UID.
[**get_library_element_connections**](LibraryElementsApi.md#get_library_element_connections) | **GET** /library-elements/{library_element_uid}/connections/ | Get library element connections.
[**get_library_elements**](LibraryElementsApi.md#get_library_elements) | **GET** /library-elements | Get all library elements.
[**update_library_element**](LibraryElementsApi.md#update_library_element) | **PATCH** /library-elements/{library_element_uid} | Update library element.


# **create_library_element**
> LibraryElementResponse create_library_element(create_library_element_command)

Create library element.

Creates a new library element.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.create_library_element_command import CreateLibraryElementCommand
from grafanaApiClient.models.library_element_response import LibraryElementResponse
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    create_library_element_command = grafanaApiClient.CreateLibraryElementCommand() # CreateLibraryElementCommand | 

    try:
        # Create library element.
        api_response = api_instance.create_library_element(create_library_element_command)
        print("The response of LibraryElementsApi->create_library_element:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->create_library_element: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_library_element_command** | [**CreateLibraryElementCommand**](CreateLibraryElementCommand.md)|  | 

### Return type

[**LibraryElementResponse**](LibraryElementResponse.md)

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

# **delete_library_element_by_uid**
> SuccessResponseBody delete_library_element_by_uid(library_element_uid)

Delete library element.

Deletes an existing library element as specified by the UID. This operation cannot be reverted. You cannot delete a library element that is connected. This operation cannot be reverted.

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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    library_element_uid = 'library_element_uid_example' # str | 

    try:
        # Delete library element.
        api_response = api_instance.delete_library_element_by_uid(library_element_uid)
        print("The response of LibraryElementsApi->delete_library_element_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->delete_library_element_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

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
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_element_by_name**
> LibraryElementResponse get_library_element_by_name(library_element_name)

Get library element by name.

Returns a library element with the given name.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.library_element_response import LibraryElementResponse
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    library_element_name = 'library_element_name_example' # str | 

    try:
        # Get library element by name.
        api_response = api_instance.get_library_element_by_name(library_element_name)
        print("The response of LibraryElementsApi->get_library_element_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->get_library_element_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_name** | **str**|  | 

### Return type

[**LibraryElementResponse**](LibraryElementResponse.md)

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

# **get_library_element_by_uid**
> LibraryElementResponse get_library_element_by_uid(library_element_uid)

Get library element by UID.

Returns a library element with the given UID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.library_element_response import LibraryElementResponse
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    library_element_uid = 'library_element_uid_example' # str | 

    try:
        # Get library element by UID.
        api_response = api_instance.get_library_element_by_uid(library_element_uid)
        print("The response of LibraryElementsApi->get_library_element_by_uid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->get_library_element_by_uid: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

### Return type

[**LibraryElementResponse**](LibraryElementResponse.md)

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

# **get_library_element_connections**
> LibraryElementConnectionsResponse get_library_element_connections(library_element_uid)

Get library element connections.

Returns a list of connections for a library element based on the UID specified.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.library_element_connections_response import LibraryElementConnectionsResponse
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    library_element_uid = 'library_element_uid_example' # str | 

    try:
        # Get library element connections.
        api_response = api_instance.get_library_element_connections(library_element_uid)
        print("The response of LibraryElementsApi->get_library_element_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->get_library_element_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 

### Return type

[**LibraryElementConnectionsResponse**](LibraryElementConnectionsResponse.md)

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

# **get_library_elements**
> LibraryElementSearchResponse get_library_elements(search_string=search_string, kind=kind, sort_direction=sort_direction, type_filter=type_filter, exclude_uid=exclude_uid, folder_filter=folder_filter, per_page=per_page, page=page)

Get all library elements.

Returns a list of all library elements the authenticated user has permission to view. Use the `perPage` query parameter to control the maximum number of library elements returned; the default limit is `100`. You can also use the `page` query parameter to fetch library elements from any page other than the first one.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.library_element_search_response import LibraryElementSearchResponse
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    search_string = 'search_string_example' # str | Part of the name or description searched for. (optional)
    kind = 56 # int | Kind of element to search for. (optional)
    sort_direction = 'sort_direction_example' # str | Sort order of elements. (optional)
    type_filter = 'type_filter_example' # str | A comma separated list of types to filter the elements by (optional)
    exclude_uid = 'exclude_uid_example' # str | Element UID to exclude from search results. (optional)
    folder_filter = 'folder_filter_example' # str | A comma separated list of folder ID(s) to filter the elements by. (optional)
    per_page = 100 # int | The number of results per page. (optional) (default to 100)
    page = 1 # int | The page for a set of records, given that only perPage records are returned at a time. Numbering starts at 1. (optional) (default to 1)

    try:
        # Get all library elements.
        api_response = api_instance.get_library_elements(search_string=search_string, kind=kind, sort_direction=sort_direction, type_filter=type_filter, exclude_uid=exclude_uid, folder_filter=folder_filter, per_page=per_page, page=page)
        print("The response of LibraryElementsApi->get_library_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->get_library_elements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Part of the name or description searched for. | [optional] 
 **kind** | **int**| Kind of element to search for. | [optional] 
 **sort_direction** | **str**| Sort order of elements. | [optional] 
 **type_filter** | **str**| A comma separated list of types to filter the elements by | [optional] 
 **exclude_uid** | **str**| Element UID to exclude from search results. | [optional] 
 **folder_filter** | **str**| A comma separated list of folder ID(s) to filter the elements by. | [optional] 
 **per_page** | **int**| The number of results per page. | [optional] [default to 100]
 **page** | **int**| The page for a set of records, given that only perPage records are returned at a time. Numbering starts at 1. | [optional] [default to 1]

### Return type

[**LibraryElementSearchResponse**](LibraryElementSearchResponse.md)

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

# **update_library_element**
> LibraryElementResponse update_library_element(library_element_uid, patch_library_element_command)

Update library element.

Updates an existing library element identified by uid.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.library_element_response import LibraryElementResponse
from grafanaApiClient.models.patch_library_element_command import PatchLibraryElementCommand
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
    api_instance = grafanaApiClient.LibraryElementsApi(api_client)
    library_element_uid = 'library_element_uid_example' # str | 
    patch_library_element_command = grafanaApiClient.PatchLibraryElementCommand() # PatchLibraryElementCommand | 

    try:
        # Update library element.
        api_response = api_instance.update_library_element(library_element_uid, patch_library_element_command)
        print("The response of LibraryElementsApi->update_library_element:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibraryElementsApi->update_library_element: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_element_uid** | **str**|  | 
 **patch_library_element_command** | [**PatchLibraryElementCommand**](PatchLibraryElementCommand.md)|  | 

### Return type

[**LibraryElementResponse**](LibraryElementResponse.md)

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
**412** | PreconditionFailedError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

