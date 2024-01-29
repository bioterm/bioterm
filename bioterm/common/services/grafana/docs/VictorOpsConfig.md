# VictorOpsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_key_file** | **str** |  | [optional] 
**api_url** | [**URL**](URL.md) |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**entity_display_name** | **str** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message_type** | **str** |  | [optional] 
**monitoring_tool** | **str** |  | [optional] 
**routing_key** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**state_message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.victor_ops_config import VictorOpsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VictorOpsConfig from a JSON string
victor_ops_config_instance = VictorOpsConfig.from_json(json)
# print the JSON string representation of the object
print VictorOpsConfig.to_json()

# convert the object into a dict
victor_ops_config_dict = victor_ops_config_instance.to_dict()
# create an instance of VictorOpsConfig from a dict
victor_ops_config_form_dict = victor_ops_config.from_dict(victor_ops_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


