# TimeRangeDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.time_range_dto import TimeRangeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeDTO from a JSON string
time_range_dto_instance = TimeRangeDTO.from_json(json)
# print the JSON string representation of the object
print TimeRangeDTO.to_json()

# convert the object into a dict
time_range_dto_dict = time_range_dto_instance.to_dict()
# create an instance of TimeRangeDTO from a dict
time_range_dto_form_dict = time_range_dto.from_dict(time_range_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


