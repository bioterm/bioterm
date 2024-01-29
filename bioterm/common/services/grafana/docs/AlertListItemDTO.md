# AlertListItemDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **int** |  | [optional] 
**dashboard_slug** | **str** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**eval_data** | **object** |  | [optional] 
**eval_date** | **datetime** |  | [optional] 
**execution_error** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**new_state_date** | **datetime** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_list_item_dto import AlertListItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AlertListItemDTO from a JSON string
alert_list_item_dto_instance = AlertListItemDTO.from_json(json)
# print the JSON string representation of the object
print AlertListItemDTO.to_json()

# convert the object into a dict
alert_list_item_dto_dict = alert_list_item_dto_instance.to_dict()
# create an instance of AlertListItemDTO from a dict
alert_list_item_dto_form_dict = alert_list_item_dto.from_dict(alert_list_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


