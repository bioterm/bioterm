# grafanaApiClient.DashboardPublicApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_public_dashboard**](DashboardPublicApi.md#create_public_dashboard) | **POST** /dashboards/uid/{dashboardUid}/public-dashboards | 
[**delete_public_dashboard**](DashboardPublicApi.md#delete_public_dashboard) | **DELETE** /dashboards/uid/{dashboardUid}/public-dashboards/{uid} | 
[**get_public_annotations**](DashboardPublicApi.md#get_public_annotations) | **GET** /public/dashboards/{accessToken}/annotations | 
[**get_public_dashboard**](DashboardPublicApi.md#get_public_dashboard) | **GET** /dashboards/uid/{dashboardUid}/public-dashboards | 
[**list_public_dashboards**](DashboardPublicApi.md#list_public_dashboards) | **GET** /dashboards/public-dashboards | 
[**query_public_dashboard**](DashboardPublicApi.md#query_public_dashboard) | **POST** /public/dashboards/{accessToken}/panels/{panelId}/query | 
[**update_public_dashboard**](DashboardPublicApi.md#update_public_dashboard) | **PATCH** /dashboards/uid/{dashboardUid}/public-dashboards/{uid} | 
[**view_public_dashboard**](DashboardPublicApi.md#view_public_dashboard) | **GET** /public/dashboards/{accessToken} | 


# **create_public_dashboard**
> PublicDashboard create_public_dashboard(dashboard_uid, public_dashboard_dto)



Create public dashboard for a dashboard

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.public_dashboard import PublicDashboard
from grafanaApiClient.models.public_dashboard_dto import PublicDashboardDTO
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    dashboard_uid = 'dashboard_uid_example' # str | 
    public_dashboard_dto = grafanaApiClient.PublicDashboardDTO() # PublicDashboardDTO | 

    try:
        api_response = api_instance.create_public_dashboard(dashboard_uid, public_dashboard_dto)
        print("The response of DashboardPublicApi->create_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->create_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_uid** | **str**|  | 
 **public_dashboard_dto** | [**PublicDashboardDTO**](PublicDashboardDTO.md)|  | 

### Return type

[**PublicDashboard**](PublicDashboard.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_public_dashboard**
> SuccessResponseBody delete_public_dashboard(dashboard_uid, uid)



Delete public dashboard for a dashboard

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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    dashboard_uid = 'dashboard_uid_example' # str | 
    uid = 'uid_example' # str | 

    try:
        api_response = api_instance.delete_public_dashboard(dashboard_uid, uid)
        print("The response of DashboardPublicApi->delete_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->delete_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_uid** | **str**|  | 
 **uid** | **str**|  | 

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
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_annotations**
> List[AnnotationEvent] get_public_annotations(access_token)



Get annotations for a public dashboard

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.annotation_event import AnnotationEvent
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    access_token = 'access_token_example' # str | 

    try:
        api_response = api_instance.get_public_annotations(access_token)
        print("The response of DashboardPublicApi->get_public_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->get_public_annotations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 

### Return type

[**List[AnnotationEvent]**](AnnotationEvent.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundPublicError is returned when the requested resource was not found. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_dashboard**
> PublicDashboard get_public_dashboard(dashboard_uid)



Get public dashboard by dashboardUid

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.public_dashboard import PublicDashboard
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    dashboard_uid = 'dashboard_uid_example' # str | 

    try:
        api_response = api_instance.get_public_dashboard(dashboard_uid)
        print("The response of DashboardPublicApi->get_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->get_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_uid** | **str**|  | 

### Return type

[**PublicDashboard**](PublicDashboard.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundPublicError is returned when the requested resource was not found. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_dashboards**
> PublicDashboardListResponseWithPagination list_public_dashboards()



Get list of public dashboards

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.public_dashboard_list_response_with_pagination import PublicDashboardListResponseWithPagination
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)

    try:
        api_response = api_instance.list_public_dashboards()
        print("The response of DashboardPublicApi->list_public_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->list_public_dashboards: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicDashboardListResponseWithPagination**](PublicDashboardListResponseWithPagination.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_public_dashboard**
> QueryDataResponse query_public_dashboard(access_token, panel_id)



Get results for a given panel on a public dashboard

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    access_token = 'access_token_example' # str | 
    panel_id = 56 # int | 

    try:
        api_response = api_instance.query_public_dashboard(access_token, panel_id)
        print("The response of DashboardPublicApi->query_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->query_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **panel_id** | **int**|  | 

### Return type

[**QueryDataResponse**](QueryDataResponse.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundPublicError is returned when the requested resource was not found. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_public_dashboard**
> PublicDashboard update_public_dashboard(dashboard_uid, uid, public_dashboard_dto)



Update public dashboard for a dashboard

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.public_dashboard import PublicDashboard
from grafanaApiClient.models.public_dashboard_dto import PublicDashboardDTO
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    dashboard_uid = 'dashboard_uid_example' # str | 
    uid = 'uid_example' # str | 
    public_dashboard_dto = grafanaApiClient.PublicDashboardDTO() # PublicDashboardDTO | 

    try:
        api_response = api_instance.update_public_dashboard(dashboard_uid, uid, public_dashboard_dto)
        print("The response of DashboardPublicApi->update_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->update_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_uid** | **str**|  | 
 **uid** | **str**|  | 
 **public_dashboard_dto** | [**PublicDashboardDTO**](PublicDashboardDTO.md)|  | 

### Return type

[**PublicDashboard**](PublicDashboard.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_public_dashboard**
> DashboardFullWithMeta view_public_dashboard(access_token)



Get public dashboard for view

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.dashboard_full_with_meta import DashboardFullWithMeta
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
    api_instance = grafanaApiClient.DashboardPublicApi(api_client)
    access_token = 'access_token_example' # str | 

    try:
        api_response = api_instance.view_public_dashboard(access_token)
        print("The response of DashboardPublicApi->view_public_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardPublicApi->view_public_dashboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 

### Return type

[**DashboardFullWithMeta**](DashboardFullWithMeta.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**400** | BadRequestPublicError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorisedPublicError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenPublicError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundPublicError is returned when the requested resource was not found. |  -  |
**500** | InternalServerPublicError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

