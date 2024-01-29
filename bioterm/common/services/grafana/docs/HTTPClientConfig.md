# HTTPClientConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**Authorization**](Authorization.md) |  | [optional] 
**basic_auth** | [**BasicAuth**](BasicAuth.md) |  | [optional] 
**bearer_token** | **str** |  | [optional] 
**bearer_token_file** | **str** | The bearer token file for the targets. Deprecated in favour of Authorization.CredentialsFile. | [optional] 
**enable_http2** | **bool** | EnableHTTP2 specifies whether the client should configure HTTP2. The omitempty flag is not set, because it would be hidden from the marshalled configuration when set to false. | [optional] 
**follow_redirects** | **bool** | FollowRedirects specifies whether the client should follow HTTP 3xx redirects. The omitempty flag is not set, because it would be hidden from the marshalled configuration when set to false. | [optional] 
**no_proxy** | **str** | NoProxy contains addresses that should not use a proxy. | [optional] 
**oauth2** | [**OAuth2**](OAuth2.md) |  | [optional] 
**proxy_connect_header** | **Dict[str, List[str]]** |  | [optional] 
**proxy_from_environment** | **bool** | ProxyFromEnvironment makes use of net/http ProxyFromEnvironment function to determine proxies. | [optional] 
**proxy_url** | [**URL**](URL.md) |  | [optional] 
**tls_config** | [**TLSConfig**](TLSConfig.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.http_client_config import HTTPClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPClientConfig from a JSON string
http_client_config_instance = HTTPClientConfig.from_json(json)
# print the JSON string representation of the object
print HTTPClientConfig.to_json()

# convert the object into a dict
http_client_config_dict = http_client_config_instance.to_dict()
# create an instance of HTTPClientConfig from a dict
http_client_config_form_dict = http_client_config.from_dict(http_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


