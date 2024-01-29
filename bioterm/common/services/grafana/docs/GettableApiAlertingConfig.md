# GettableApiAlertingConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**GlobalConfig**](GlobalConfig.md) |  | [optional] 
**inhibit_rules** | [**List[InhibitRule]**](InhibitRule.md) |  | [optional] 
**mute_time_provenances** | **Dict[str, str]** |  | [optional] 
**mute_time_intervals** | [**List[MuteTimeInterval]**](MuteTimeInterval.md) |  | [optional] 
**receivers** | [**List[GettableApiReceiver]**](GettableApiReceiver.md) | Override with our superset receiver type | [optional] 
**route** | [**Route**](Route.md) |  | [optional] 
**templates** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_api_alerting_config import GettableApiAlertingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GettableApiAlertingConfig from a JSON string
gettable_api_alerting_config_instance = GettableApiAlertingConfig.from_json(json)
# print the JSON string representation of the object
print GettableApiAlertingConfig.to_json()

# convert the object into a dict
gettable_api_alerting_config_dict = gettable_api_alerting_config_instance.to_dict()
# create an instance of GettableApiAlertingConfig from a dict
gettable_api_alerting_config_form_dict = gettable_api_alerting_config.from_dict(gettable_api_alerting_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


