# MuteTimeInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**time_intervals** | [**List[TimeInterval]**](TimeInterval.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.mute_time_interval import MuteTimeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of MuteTimeInterval from a JSON string
mute_time_interval_instance = MuteTimeInterval.from_json(json)
# print the JSON string representation of the object
print MuteTimeInterval.to_json()

# convert the object into a dict
mute_time_interval_dict = mute_time_interval_instance.to_dict()
# create an instance of MuteTimeInterval from a dict
mute_time_interval_form_dict = mute_time_interval.from_dict(mute_time_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


