# grafanaApiClient.AnnotationsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_annotation_by_id**](AnnotationsApi.md#delete_annotation_by_id) | **DELETE** /annotations/{annotation_id} | Delete Annotation By ID.
[**get_annotation_by_id**](AnnotationsApi.md#get_annotation_by_id) | **GET** /annotations/{annotation_id} | Get Annotation by ID.
[**get_annotation_tags**](AnnotationsApi.md#get_annotation_tags) | **GET** /annotations/tags | Find Annotations Tags.
[**get_annotations**](AnnotationsApi.md#get_annotations) | **GET** /annotations | Find Annotations.
[**mass_delete_annotations**](AnnotationsApi.md#mass_delete_annotations) | **POST** /annotations/mass-delete | Delete multiple annotations.
[**patch_annotation**](AnnotationsApi.md#patch_annotation) | **PATCH** /annotations/{annotation_id} | Patch Annotation.
[**post_annotation**](AnnotationsApi.md#post_annotation) | **POST** /annotations | Create Annotation.
[**post_graphite_annotation**](AnnotationsApi.md#post_graphite_annotation) | **POST** /annotations/graphite | Create Annotation in Graphite format.
[**update_annotation**](AnnotationsApi.md#update_annotation) | **PUT** /annotations/{annotation_id} | Update Annotation.


# **delete_annotation_by_id**
> SuccessResponseBody delete_annotation_by_id(annotation_id)

Delete Annotation By ID.

Deletes the annotation that matches the specified ID.

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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | 

    try:
        # Delete Annotation By ID.
        api_response = api_instance.delete_annotation_by_id(annotation_id)
        print("The response of AnnotationsApi->delete_annotation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->delete_annotation_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotation_by_id**
> Annotation get_annotation_by_id(annotation_id)

Get Annotation by ID.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.annotation import Annotation
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | 

    try:
        # Get Annotation by ID.
        api_response = api_instance.get_annotation_by_id(annotation_id)
        print("The response of AnnotationsApi->get_annotation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->get_annotation_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 

### Return type

[**Annotation**](Annotation.md)

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

# **get_annotation_tags**
> GetAnnotationTagsResponse get_annotation_tags(tag=tag, limit=limit)

Find Annotations Tags.

Find all the event tags created in the annotations.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.get_annotation_tags_response import GetAnnotationTagsResponse
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    tag = 'tag_example' # str | Tag is a string that you can use to filter tags. (optional)
    limit = '100' # str | Max limit for results returned. (optional) (default to '100')

    try:
        # Find Annotations Tags.
        api_response = api_instance.get_annotation_tags(tag=tag, limit=limit)
        print("The response of AnnotationsApi->get_annotation_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->get_annotation_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag is a string that you can use to filter tags. | [optional] 
 **limit** | **str**| Max limit for results returned. | [optional] [default to &#39;100&#39;]

### Return type

[**GetAnnotationTagsResponse**](GetAnnotationTagsResponse.md)

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

# **get_annotations**
> List[Annotation] get_annotations(var_from=var_from, to=to, user_id=user_id, alert_id=alert_id, dashboard_id=dashboard_id, dashboard_uid=dashboard_uid, panel_id=panel_id, limit=limit, tags=tags, type=type, match_any=match_any)

Find Annotations.

Starting in Grafana v6.4 regions annotations are now returned in one entity that now includes the timeEnd property.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.annotation import Annotation
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    var_from = 56 # int | Find annotations created after specific epoch datetime in milliseconds. (optional)
    to = 56 # int | Find annotations created before specific epoch datetime in milliseconds. (optional)
    user_id = 56 # int | Limit response to annotations created by specific user. (optional)
    alert_id = 56 # int | Find annotations for a specified alert. (optional)
    dashboard_id = 56 # int | Find annotations that are scoped to a specific dashboard (optional)
    dashboard_uid = 'dashboard_uid_example' # str | Find annotations that are scoped to a specific dashboard (optional)
    panel_id = 56 # int | Find annotations that are scoped to a specific panel (optional)
    limit = 56 # int | Max limit for results returned. (optional)
    tags = ['tags_example'] # List[str] | Use this to filter organization annotations. Organization annotations are annotations from an annotation data source that are not connected specifically to a dashboard or panel. You can filter by multiple tags. (optional)
    type = 'type_example' # str | Return alerts or user created annotations (optional)
    match_any = True # bool | Match any or all tags (optional)

    try:
        # Find Annotations.
        api_response = api_instance.get_annotations(var_from=var_from, to=to, user_id=user_id, alert_id=alert_id, dashboard_id=dashboard_id, dashboard_uid=dashboard_uid, panel_id=panel_id, limit=limit, tags=tags, type=type, match_any=match_any)
        print("The response of AnnotationsApi->get_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->get_annotations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**| Find annotations created after specific epoch datetime in milliseconds. | [optional] 
 **to** | **int**| Find annotations created before specific epoch datetime in milliseconds. | [optional] 
 **user_id** | **int**| Limit response to annotations created by specific user. | [optional] 
 **alert_id** | **int**| Find annotations for a specified alert. | [optional] 
 **dashboard_id** | **int**| Find annotations that are scoped to a specific dashboard | [optional] 
 **dashboard_uid** | **str**| Find annotations that are scoped to a specific dashboard | [optional] 
 **panel_id** | **int**| Find annotations that are scoped to a specific panel | [optional] 
 **limit** | **int**| Max limit for results returned. | [optional] 
 **tags** | [**List[str]**](str.md)| Use this to filter organization annotations. Organization annotations are annotations from an annotation data source that are not connected specifically to a dashboard or panel. You can filter by multiple tags. | [optional] 
 **type** | **str**| Return alerts or user created annotations | [optional] 
 **match_any** | **bool**| Match any or all tags | [optional] 

### Return type

[**List[Annotation]**](Annotation.md)

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

# **mass_delete_annotations**
> SuccessResponseBody mass_delete_annotations(mass_delete_annotations_cmd)

Delete multiple annotations.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.mass_delete_annotations_cmd import MassDeleteAnnotationsCmd
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    mass_delete_annotations_cmd = grafanaApiClient.MassDeleteAnnotationsCmd() # MassDeleteAnnotationsCmd | 

    try:
        # Delete multiple annotations.
        api_response = api_instance.mass_delete_annotations(mass_delete_annotations_cmd)
        print("The response of AnnotationsApi->mass_delete_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->mass_delete_annotations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_delete_annotations_cmd** | [**MassDeleteAnnotationsCmd**](MassDeleteAnnotationsCmd.md)|  | 

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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_annotation**
> SuccessResponseBody patch_annotation(annotation_id, patch_annotations_cmd)

Patch Annotation.

Updates one or more properties of an annotation that matches the specified ID. This operation currently supports updating of the `text`, `tags`, `time` and `timeEnd` properties. This is available in Grafana 6.0.0-beta2 and above.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.patch_annotations_cmd import PatchAnnotationsCmd
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | 
    patch_annotations_cmd = grafanaApiClient.PatchAnnotationsCmd() # PatchAnnotationsCmd | 

    try:
        # Patch Annotation.
        api_response = api_instance.patch_annotation(annotation_id, patch_annotations_cmd)
        print("The response of AnnotationsApi->patch_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->patch_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 
 **patch_annotations_cmd** | [**PatchAnnotationsCmd**](PatchAnnotationsCmd.md)|  | 

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
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_annotation**
> PostAnnotation200Response post_annotation(post_annotations_cmd)

Create Annotation.

Creates an annotation in the Grafana database. The dashboardId and panelId fields are optional. If they are not specified then an organization annotation is created and can be queried in any dashboard that adds the Grafana annotations data source. When creating a region annotation include the timeEnd property. The format for `time` and `timeEnd` should be epoch numbers in millisecond resolution. The response for this HTTP request is slightly different in versions prior to v6.4. In prior versions you would also get an endId if you where creating a region. But in 6.4 regions are represented using a single event with time and timeEnd properties.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.post_annotation200_response import PostAnnotation200Response
from grafanaApiClient.models.post_annotations_cmd import PostAnnotationsCmd
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    post_annotations_cmd = grafanaApiClient.PostAnnotationsCmd() # PostAnnotationsCmd | 

    try:
        # Create Annotation.
        api_response = api_instance.post_annotation(post_annotations_cmd)
        print("The response of AnnotationsApi->post_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->post_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_annotations_cmd** | [**PostAnnotationsCmd**](PostAnnotationsCmd.md)|  | 

### Return type

[**PostAnnotation200Response**](PostAnnotation200Response.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_graphite_annotation**
> PostAnnotation200Response post_graphite_annotation(post_graphite_annotations_cmd)

Create Annotation in Graphite format.

Creates an annotation by using Graphite-compatible event format. The `when` and `data` fields are optional. If `when` is not specified then the current time will be used as annotation’s timestamp. The `tags` field can also be in prior to Graphite `0.10.0` format (string with multiple tags being separated by a space).

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.post_annotation200_response import PostAnnotation200Response
from grafanaApiClient.models.post_graphite_annotations_cmd import PostGraphiteAnnotationsCmd
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    post_graphite_annotations_cmd = grafanaApiClient.PostGraphiteAnnotationsCmd() # PostGraphiteAnnotationsCmd | 

    try:
        # Create Annotation in Graphite format.
        api_response = api_instance.post_graphite_annotation(post_graphite_annotations_cmd)
        print("The response of AnnotationsApi->post_graphite_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->post_graphite_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_graphite_annotations_cmd** | [**PostGraphiteAnnotationsCmd**](PostGraphiteAnnotationsCmd.md)|  | 

### Return type

[**PostAnnotation200Response**](PostAnnotation200Response.md)

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> SuccessResponseBody update_annotation(annotation_id, update_annotations_cmd)

Update Annotation.

Updates all properties of an annotation that matches the specified id. To only update certain property, consider using the Patch Annotation operation.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.models.update_annotations_cmd import UpdateAnnotationsCmd
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
    api_instance = grafanaApiClient.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | 
    update_annotations_cmd = grafanaApiClient.UpdateAnnotationsCmd() # UpdateAnnotationsCmd | 

    try:
        # Update Annotation.
        api_response = api_instance.update_annotation(annotation_id, update_annotations_cmd)
        print("The response of AnnotationsApi->update_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->update_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | **str**|  | 
 **update_annotations_cmd** | [**UpdateAnnotationsCmd**](UpdateAnnotationsCmd.md)|  | 

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

