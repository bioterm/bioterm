# PostableApiAlertingConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**GlobalConfig**](GlobalConfig.md) |  | [optional] 
**inhibit_rules** | [**List[InhibitRule]**](InhibitRule.md) |  | [optional] 
**mute_time_intervals** | [**List[MuteTimeInterval]**](MuteTimeInterval.md) |  | [optional] 
**receivers** | [**List[PostableApiReceiver]**](PostableApiReceiver.md) | Override with our superset receiver type | [optional] 
**route** | [**Route**](Route.md) |  | [optional] 
**templates** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_api_alerting_config import PostableApiAlertingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostableApiAlertingConfig from a JSON string
postable_api_alerting_config_instance = PostableApiAlertingConfig.from_json(json)
# print the JSON string representation of the object
print PostableApiAlertingConfig.to_json()

# convert the object into a dict
postable_api_alerting_config_dict = postable_api_alerting_config_instance.to_dict()
# create an instance of PostableApiAlertingConfig from a dict
postable_api_alerting_config_form_dict = postable_api_alerting_config.from_dict(postable_api_alerting_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


