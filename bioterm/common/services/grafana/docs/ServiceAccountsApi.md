# grafanaApiClient.ServiceAccountsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_account**](ServiceAccountsApi.md#create_service_account) | **POST** /serviceaccounts | Create service account
[**create_token**](ServiceAccountsApi.md#create_token) | **POST** /serviceaccounts/{serviceAccountId}/tokens | CreateNewToken adds a token to a service account
[**delete_service_account**](ServiceAccountsApi.md#delete_service_account) | **DELETE** /serviceaccounts/{serviceAccountId} | Delete service account
[**delete_token**](ServiceAccountsApi.md#delete_token) | **DELETE** /serviceaccounts/{serviceAccountId}/tokens/{tokenId} | DeleteToken deletes service account tokens
[**list_tokens**](ServiceAccountsApi.md#list_tokens) | **GET** /serviceaccounts/{serviceAccountId}/tokens | Get service account tokens
[**retrieve_service_account**](ServiceAccountsApi.md#retrieve_service_account) | **GET** /serviceaccounts/{serviceAccountId} | Get single serviceaccount by Id
[**search_org_service_accounts_with_paging**](ServiceAccountsApi.md#search_org_service_accounts_with_paging) | **GET** /serviceaccounts/search | Search service accounts with paging
[**update_service_account**](ServiceAccountsApi.md#update_service_account) | **PATCH** /serviceaccounts/{serviceAccountId} | Update service account


# **create_service_account**
> ServiceAccountDTO create_service_account(create_service_account_form=create_service_account_form)

Create service account

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:write` scope: `serviceaccounts:*`  Requires basic authentication and that the authenticated user is a Grafana Admin.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.create_service_account_form import CreateServiceAccountForm
from grafanaApiClient.models.service_account_dto import ServiceAccountDTO
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    create_service_account_form = grafanaApiClient.CreateServiceAccountForm() # CreateServiceAccountForm |  (optional)

    try:
        # Create service account
        api_response = api_instance.create_service_account(create_service_account_form=create_service_account_form)
        print("The response of ServiceAccountsApi->create_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_service_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_account_form** | [**CreateServiceAccountForm**](CreateServiceAccountForm.md)|  | [optional] 

### Return type

[**ServiceAccountDTO**](ServiceAccountDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (empty) |  -  |
**400** | BadRequestError is returned when the request is invalid and it cannot be processed. |  -  |
**401** | UnauthorizedError is returned when the request is not authenticated. |  -  |
**403** | ForbiddenError is returned if the user/token has insufficient permissions to access the requested resource. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> NewApiKeyResult create_token(service_account_id, add_service_account_token_command=add_service_account_token_command)

CreateNewToken adds a token to a service account

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:write` scope: `serviceaccounts:id:1` (single service account)

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.add_service_account_token_command import AddServiceAccountTokenCommand
from grafanaApiClient.models.new_api_key_result import NewApiKeyResult
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | 
    add_service_account_token_command = grafanaApiClient.AddServiceAccountTokenCommand() # AddServiceAccountTokenCommand |  (optional)

    try:
        # CreateNewToken adds a token to a service account
        api_response = api_instance.create_token(service_account_id, add_service_account_token_command=add_service_account_token_command)
        print("The response of ServiceAccountsApi->create_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**|  | 
 **add_service_account_token_command** | [**AddServiceAccountTokenCommand**](AddServiceAccountTokenCommand.md)|  | [optional] 

### Return type

[**NewApiKeyResult**](NewApiKeyResult.md)

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
**409** | ConflictError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_account**
> SuccessResponseBody delete_service_account(service_account_id)

Delete service account

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:delete` scope: `serviceaccounts:id:1` (single service account)

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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | 

    try:
        # Delete service account
        api_response = api_instance.delete_service_account(service_account_id)
        print("The response of ServiceAccountsApi->delete_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->delete_service_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**|  | 

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
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> SuccessResponseBody delete_token(token_id, service_account_id)

DeleteToken deletes service account tokens

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:write` scope: `serviceaccounts:id:1` (single service account)  Requires basic authentication and that the authenticated user is a Grafana Admin.

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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    token_id = 56 # int | 
    service_account_id = 56 # int | 

    try:
        # DeleteToken deletes service account tokens
        api_response = api_instance.delete_token(token_id, service_account_id)
        print("The response of ServiceAccountsApi->delete_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->delete_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 
 **service_account_id** | **int**|  | 

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

# **list_tokens**
> List[TokenDTO] list_tokens(service_account_id)

Get service account tokens

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:read` scope: `global:serviceaccounts:id:1` (single service account)  Requires basic authentication and that the authenticated user is a Grafana Admin.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.token_dto import TokenDTO
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | 

    try:
        # Get service account tokens
        api_response = api_instance.list_tokens(service_account_id)
        print("The response of ServiceAccountsApi->list_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->list_tokens: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**|  | 

### Return type

[**List[TokenDTO]**](TokenDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **retrieve_service_account**
> ServiceAccountDTO retrieve_service_account(service_account_id)

Get single serviceaccount by Id

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:read` scope: `serviceaccounts:id:1` (single service account)

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.service_account_dto import ServiceAccountDTO
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | 

    try:
        # Get single serviceaccount by Id
        api_response = api_instance.retrieve_service_account(service_account_id)
        print("The response of ServiceAccountsApi->retrieve_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->retrieve_service_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**|  | 

### Return type

[**ServiceAccountDTO**](ServiceAccountDTO.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **search_org_service_accounts_with_paging**
> SearchOrgServiceAccountsResult search_org_service_accounts_with_paging(disabled=disabled, expired_tokens=expired_tokens, query=query, perpage=perpage, page=page)

Search service accounts with paging

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:read` scope: `serviceaccounts:*`

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.search_org_service_accounts_result import SearchOrgServiceAccountsResult
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    disabled = True # bool |  (optional)
    expired_tokens = True # bool |  (optional)
    query = 'query_example' # str | It will return results where the query value is contained in one of the name. Query values with spaces need to be URL encoded. (optional)
    perpage = 56 # int | The default value is 1000. (optional)
    page = 56 # int | The default value is 1. (optional)

    try:
        # Search service accounts with paging
        api_response = api_instance.search_org_service_accounts_with_paging(disabled=disabled, expired_tokens=expired_tokens, query=query, perpage=perpage, page=page)
        print("The response of ServiceAccountsApi->search_org_service_accounts_with_paging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->search_org_service_accounts_with_paging: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disabled** | **bool**|  | [optional] 
 **expired_tokens** | **bool**|  | [optional] 
 **query** | **str**| It will return results where the query value is contained in one of the name. Query values with spaces need to be URL encoded. | [optional] 
 **perpage** | **int**| The default value is 1000. | [optional] 
 **page** | **int**| The default value is 1. | [optional] 

### Return type

[**SearchOrgServiceAccountsResult**](SearchOrgServiceAccountsResult.md)

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

# **update_service_account**
> UpdateServiceAccount200Response update_service_account(service_account_id, update_service_account_form=update_service_account_form)

Update service account

Required permissions (See note in the [introduction](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api) for an explanation): action: `serviceaccounts:write` scope: `serviceaccounts:id:1` (single service account)

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.update_service_account200_response import UpdateServiceAccount200Response
from grafanaApiClient.models.update_service_account_form import UpdateServiceAccountForm
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
    api_instance = grafanaApiClient.ServiceAccountsApi(api_client)
    service_account_id = 56 # int | 
    update_service_account_form = grafanaApiClient.UpdateServiceAccountForm() # UpdateServiceAccountForm |  (optional)

    try:
        # Update service account
        api_response = api_instance.update_service_account(service_account_id, update_service_account_form=update_service_account_form)
        print("The response of ServiceAccountsApi->update_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->update_service_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_id** | **int**|  | 
 **update_service_account_form** | [**UpdateServiceAccountForm**](UpdateServiceAccountForm.md)|  | [optional] 

### Return type

[**UpdateServiceAccount200Response**](UpdateServiceAccount200Response.md)

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

