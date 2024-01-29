# grafanaApiClient.AdminUsersApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_create_user**](AdminUsersApi.md#admin_create_user) | **POST** /admin/users | Create new user.
[**admin_delete_user**](AdminUsersApi.md#admin_delete_user) | **DELETE** /admin/users/{user_id} | Delete global User.
[**admin_disable_user**](AdminUsersApi.md#admin_disable_user) | **POST** /admin/users/{user_id}/disable | Disable user.
[**admin_enable_user**](AdminUsersApi.md#admin_enable_user) | **POST** /admin/users/{user_id}/enable | Enable user.
[**admin_get_user_auth_tokens**](AdminUsersApi.md#admin_get_user_auth_tokens) | **GET** /admin/users/{user_id}/auth-tokens | Return a list of all auth tokens (devices) that the user currently have logged in from.
[**admin_logout_user**](AdminUsersApi.md#admin_logout_user) | **POST** /admin/users/{user_id}/logout | Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.
[**admin_revoke_user_auth_token**](AdminUsersApi.md#admin_revoke_user_auth_token) | **POST** /admin/users/{user_id}/revoke-auth-token | Revoke auth token for user.
[**admin_update_user_password**](AdminUsersApi.md#admin_update_user_password) | **PUT** /admin/users/{user_id}/password | Set password for user.
[**admin_update_user_permissions**](AdminUsersApi.md#admin_update_user_permissions) | **PUT** /admin/users/{user_id}/permissions | Set permissions for user.
[**get_user_quota**](AdminUsersApi.md#get_user_quota) | **GET** /admin/users/{user_id}/quotas | Fetch user quota.
[**update_user_quota**](AdminUsersApi.md#update_user_quota) | **PUT** /admin/users/{user_id}/quotas/{quota_target} | Update user quota.


# **admin_create_user**
> AdminCreateUserResponse admin_create_user(admin_create_user_form)

Create new user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:create`. Note that OrgId is an optional parameter that can be used to assign a new user to a different organization when `auto_assign_org` is set to `true`.

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.admin_create_user_form import AdminCreateUserForm
from grafanaApiClient.models.admin_create_user_response import AdminCreateUserResponse
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    admin_create_user_form = grafanaApiClient.AdminCreateUserForm() # AdminCreateUserForm | 

    try:
        # Create new user.
        api_response = api_instance.admin_create_user(admin_create_user_form)
        print("The response of AdminUsersApi->admin_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_create_user_form** | [**AdminCreateUserForm**](AdminCreateUserForm.md)|  | 

### Return type

[**AdminCreateUserResponse**](AdminCreateUserResponse.md)

### Authorization

[basic](../README.md#basic)

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
**412** | PreconditionFailedError |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_delete_user**
> SuccessResponseBody admin_delete_user(user_id)

Delete global User.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:delete` and scope `global.users:*`.

### Example

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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Delete global User.
        api_response = api_instance.admin_delete_user(user_id)
        print("The response of AdminUsersApi->admin_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **admin_disable_user**
> SuccessResponseBody admin_disable_user(user_id)

Disable user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:disable` and scope `global.users:1` (userIDScope).

### Example

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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Disable user.
        api_response = api_instance.admin_disable_user(user_id)
        print("The response of AdminUsersApi->admin_disable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_disable_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **admin_enable_user**
> SuccessResponseBody admin_enable_user(user_id)

Enable user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users:enable` and scope `global.users:1` (userIDScope).

### Example

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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Enable user.
        api_response = api_instance.admin_enable_user(user_id)
        print("The response of AdminUsersApi->admin_enable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_enable_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **admin_get_user_auth_tokens**
> List[UserToken] admin_get_user_auth_tokens(user_id)

Return a list of all auth tokens (devices) that the user currently have logged in from.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.authtoken:list` and scope `global.users:*`.

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.user_token import UserToken
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Return a list of all auth tokens (devices) that the user currently have logged in from.
        api_response = api_instance.admin_get_user_auth_tokens(user_id)
        print("The response of AdminUsersApi->admin_get_user_auth_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_get_user_auth_tokens: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**List[UserToken]**](UserToken.md)

### Authorization

[basic](../README.md#basic)

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

# **admin_logout_user**
> SuccessResponseBody admin_logout_user(user_id)

Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.logout` and scope `global.users:*`.

### Example

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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Logout user revokes all auth tokens (devices) for the user. User of issued auth tokens (devices) will no longer be logged in and will be required to authenticate again upon next activity.
        api_response = api_instance.admin_logout_user(user_id)
        print("The response of AdminUsersApi->admin_logout_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_logout_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

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

# **admin_revoke_user_auth_token**
> SuccessResponseBody admin_revoke_user_auth_token(user_id, revoke_auth_token_cmd)

Revoke auth token for user.

Revokes the given auth token (device) for the user. User of issued auth token (device) will no longer be logged in and will be required to authenticate again upon next activity. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.authtoken:update` and scope `global.users:*`.

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.revoke_auth_token_cmd import RevokeAuthTokenCmd
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 
    revoke_auth_token_cmd = grafanaApiClient.RevokeAuthTokenCmd() # RevokeAuthTokenCmd | 

    try:
        # Revoke auth token for user.
        api_response = api_instance.admin_revoke_user_auth_token(user_id, revoke_auth_token_cmd)
        print("The response of AdminUsersApi->admin_revoke_user_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_revoke_user_auth_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **revoke_auth_token_cmd** | [**RevokeAuthTokenCmd**](RevokeAuthTokenCmd.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

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
**404** | NotFoundError is returned when the requested resource was not found. |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_user_password**
> SuccessResponseBody admin_update_user_password(user_id, admin_update_user_password_form)

Set password for user.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.password:update` and scope `global.users:*`.

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.admin_update_user_password_form import AdminUpdateUserPasswordForm
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 
    admin_update_user_password_form = grafanaApiClient.AdminUpdateUserPasswordForm() # AdminUpdateUserPasswordForm | 

    try:
        # Set password for user.
        api_response = api_instance.admin_update_user_password(user_id, admin_update_user_password_form)
        print("The response of AdminUsersApi->admin_update_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_update_user_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **admin_update_user_password_form** | [**AdminUpdateUserPasswordForm**](AdminUpdateUserPasswordForm.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

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

# **admin_update_user_permissions**
> SuccessResponseBody admin_update_user_permissions(user_id, admin_update_user_permissions_form)

Set permissions for user.

Only works with Basic Authentication (username and password). See introduction for an explanation. If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.permissions:update` and scope `global.users:*`.

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.admin_update_user_permissions_form import AdminUpdateUserPermissionsForm
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
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 
    admin_update_user_permissions_form = grafanaApiClient.AdminUpdateUserPermissionsForm() # AdminUpdateUserPermissionsForm | 

    try:
        # Set permissions for user.
        api_response = api_instance.admin_update_user_permissions(user_id, admin_update_user_permissions_form)
        print("The response of AdminUsersApi->admin_update_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->admin_update_user_permissions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **admin_update_user_permissions_form** | [**AdminUpdateUserPermissionsForm**](AdminUpdateUserPermissionsForm.md)|  | 

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

# **get_user_quota**
> List[QuotaDTO] get_user_quota(user_id)

Fetch user quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.quotas:list` and scope `global.users:1` (userIDScope).

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.quota_dto import QuotaDTO
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Fetch user quota.
        api_response = api_instance.get_user_quota(user_id)
        print("The response of AdminUsersApi->get_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->get_user_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**List[QuotaDTO]**](QuotaDTO.md)

### Authorization

[basic](../README.md#basic)

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

# **update_user_quota**
> SuccessResponseBody update_user_quota(quota_target, user_id, update_quota_cmd)

Update user quota.

If you are running Grafana Enterprise and have Fine-grained access control enabled, you need to have a permission with action `users.quotas:update` and scope `global.users:1` (userIDScope).

### Example

* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.success_response_body import SuccessResponseBody
from grafanaApiClient.models.update_quota_cmd import UpdateQuotaCmd
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

# Configure HTTP basic authorization: basic
configuration = grafanaApiClient.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with grafanaApiClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grafanaApiClient.AdminUsersApi(api_client)
    quota_target = 'quota_target_example' # str | 
    user_id = 56 # int | 
    update_quota_cmd = grafanaApiClient.UpdateQuotaCmd() # UpdateQuotaCmd | 

    try:
        # Update user quota.
        api_response = api_instance.update_user_quota(quota_target, user_id, update_quota_cmd)
        print("The response of AdminUsersApi->update_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->update_user_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_target** | **str**|  | 
 **user_id** | **int**|  | 
 **update_quota_cmd** | [**UpdateQuotaCmd**](UpdateQuotaCmd.md)|  | 

### Return type

[**SuccessResponseBody**](SuccessResponseBody.md)

### Authorization

[basic](../README.md#basic)

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

