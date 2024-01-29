# WebexConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | [**URL**](URL.md) |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**room_id** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.webex_config import WebexConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebexConfig from a JSON string
webex_config_instance = WebexConfig.from_json(json)
# print the JSON string representation of the object
print WebexConfig.to_json()

# convert the object into a dict
webex_config_dict = webex_config_instance.to_dict()
# create an instance of WebexConfig from a dict
webex_config_form_dict = webex_config.from_dict(webex_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


