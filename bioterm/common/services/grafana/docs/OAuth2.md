# OAuth2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls_config** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**client_secret_file** | **str** |  | [optional] 
**endpoint_params** | **Dict[str, str]** |  | [optional] 
**no_proxy** | **str** | NoProxy contains addresses that should not use a proxy. | [optional] 
**proxy_connect_header** | **Dict[str, List[str]]** |  | [optional] 
**proxy_from_environment** | **bool** | ProxyFromEnvironment makes use of net/http ProxyFromEnvironment function to determine proxies. | [optional] 
**proxy_url** | [**URL**](URL.md) |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**token_url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.o_auth2 import OAuth2

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2 from a JSON string
o_auth2_instance = OAuth2.from_json(json)
# print the JSON string representation of the object
print OAuth2.to_json()

# convert the object into a dict
o_auth2_dict = o_auth2_instance.to_dict()
# create an instance of OAuth2 from a dict
o_auth2_form_dict = o_auth2.from_dict(o_auth2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


