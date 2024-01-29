# ScheduleDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** |  | [optional] 
**day_of_month** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**frequency** | **str** |  | [optional] 
**hour** | **int** |  | [optional] 
**interval_amount** | **int** |  | [optional] 
**interval_frequency** | **str** |  | [optional] 
**minute** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**workdays_only** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.schedule_dto import ScheduleDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDTO from a JSON string
schedule_dto_instance = ScheduleDTO.from_json(json)
# print the JSON string representation of the object
print ScheduleDTO.to_json()

# convert the object into a dict
schedule_dto_dict = schedule_dto_instance.to_dict()
# create an instance of ScheduleDTO from a dict
schedule_dto_form_dict = schedule_dto.from_dict(schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


