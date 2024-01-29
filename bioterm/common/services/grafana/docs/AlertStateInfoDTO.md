# AlertStateInfoDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**new_state_date** | **datetime** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_state_info_dto import AlertStateInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AlertStateInfoDTO from a JSON string
alert_state_info_dto_instance = AlertStateInfoDTO.from_json(json)
# print the JSON string representation of the object
print AlertStateInfoDTO.to_json()

# convert the object into a dict
alert_state_info_dto_dict = alert_state_info_dto_instance.to_dict()
# create an instance of AlertStateInfoDTO from a dict
alert_state_info_dto_form_dict = alert_state_info_dto.from_dict(alert_state_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


