# OpsGenieConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**api_key_file** | **str** |  | [optional] 
**api_url** | [**URL**](URL.md) |  | [optional] 
**description** | **str** |  | [optional] 
**details** | **Dict[str, str]** |  | [optional] 
**entity** | **str** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**responders** | [**List[OpsGenieConfigResponder]**](OpsGenieConfigResponder.md) |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**tags** | **str** |  | [optional] 
**update_alerts** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.ops_genie_config import OpsGenieConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OpsGenieConfig from a JSON string
ops_genie_config_instance = OpsGenieConfig.from_json(json)
# print the JSON string representation of the object
print OpsGenieConfig.to_json()

# convert the object into a dict
ops_genie_config_dict = ops_genie_config_instance.to_dict()
# create an instance of OpsGenieConfig from a dict
ops_genie_config_form_dict = ops_genie_config.from_dict(ops_genie_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


