# grafanaApiClient.SigningKeysApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_jwks**](SigningKeysApi.md#retrieve_jwks) | **GET** /signing-keys/keys | Get JSON Web Key Set (JWKS) with all the keys that can be used to verify tokens (public keys)


# **retrieve_jwks**
> RetrieveJWKS200Response retrieve_jwks()

Get JSON Web Key Set (JWKS) with all the keys that can be used to verify tokens (public keys)

Required permissions None

### Example

* Api Key Authentication (api_key):
* Basic Authentication (basic):
```python
import time
import os
import grafanaApiClient
from grafanaApiClient.models.retrieve_jwks200_response import RetrieveJWKS200Response
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
    api_instance = grafanaApiClient.SigningKeysApi(api_client)

    try:
        # Get JSON Web Key Set (JWKS) with all the keys that can be used to verify tokens (public keys)
        api_response = api_instance.retrieve_jwks()
        print("The response of SigningKeysApi->retrieve_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SigningKeysApi->retrieve_jwks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**RetrieveJWKS200Response**](RetrieveJWKS200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (empty) |  -  |
**500** | InternalServerError is a general error indicating something went wrong internally. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

