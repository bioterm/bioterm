# PublicDashboard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**annotations_enabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **int** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**recipients** | [**List[EmailDTO]**](EmailDTO.md) |  | [optional] 
**share** | **str** |  | [optional] 
**time_selection_enabled** | **bool** |  | [optional] 
**uid** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.public_dashboard import PublicDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of PublicDashboard from a JSON string
public_dashboard_instance = PublicDashboard.from_json(json)
# print the JSON string representation of the object
print PublicDashboard.to_json()

# convert the object into a dict
public_dashboard_dict = public_dashboard_instance.to_dict()
# create an instance of PublicDashboard from a dict
public_dashboard_form_dict = public_dashboard.from_dict(public_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


