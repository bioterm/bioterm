# PushoverConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | [optional] 
**expire** | **str** |  | [optional] 
**html** | **bool** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**retry** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**sound** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**token_file** | **str** |  | [optional] 
**ttl** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_title** | **str** |  | [optional] 
**user_key** | **str** |  | [optional] 
**user_key_file** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.pushover_config import PushoverConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PushoverConfig from a JSON string
pushover_config_instance = PushoverConfig.from_json(json)
# print the JSON string representation of the object
print PushoverConfig.to_json()

# convert the object into a dict
pushover_config_dict = pushover_config_instance.to_dict()
# create an instance of PushoverConfig from a dict
pushover_config_form_dict = pushover_config.from_dict(pushover_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


