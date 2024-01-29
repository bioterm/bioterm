# TimeInterval

TimeInterval describes intervals of time. ContainsTime will tell you if a golang time is contained within the interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_month** | **List[str]** |  | [optional] 
**location** | **str** |  | [optional] 
**months** | **List[str]** |  | [optional] 
**times** | [**List[TimeRange]**](TimeRange.md) |  | [optional] 
**weekdays** | **List[str]** |  | [optional] 
**years** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.time_interval import TimeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of TimeInterval from a JSON string
time_interval_instance = TimeInterval.from_json(json)
# print the JSON string representation of the object
print TimeInterval.to_json()

# convert the object into a dict
time_interval_dict = time_interval_instance.to_dict()
# create an instance of TimeInterval from a dict
time_interval_form_dict = time_interval.from_dict(time_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


