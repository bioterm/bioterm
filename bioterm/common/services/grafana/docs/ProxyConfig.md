# ProxyConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_proxy** | **str** | NoProxy contains addresses that should not use a proxy. | [optional] 
**proxy_connect_header** | **Dict[str, List[str]]** |  | [optional] 
**proxy_from_environment** | **bool** | ProxyFromEnvironment makes use of net/http ProxyFromEnvironment function to determine proxies. | [optional] 
**proxy_url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.proxy_config import ProxyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyConfig from a JSON string
proxy_config_instance = ProxyConfig.from_json(json)
# print the JSON string representation of the object
print ProxyConfig.to_json()

# convert the object into a dict
proxy_config_dict = proxy_config_instance.to_dict()
# create an instance of ProxyConfig from a dict
proxy_config_form_dict = proxy_config.from_dict(proxy_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


