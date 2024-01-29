# PublicDashboardDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**annotations_enabled** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**share** | **str** |  | [optional] 
**time_selection_enabled** | **bool** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.public_dashboard_dto import PublicDashboardDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PublicDashboardDTO from a JSON string
public_dashboard_dto_instance = PublicDashboardDTO.from_json(json)
# print the JSON string representation of the object
print PublicDashboardDTO.to_json()

# convert the object into a dict
public_dashboard_dto_dict = public_dashboard_dto_instance.to_dict()
# create an instance of PublicDashboardDTO from a dict
public_dashboard_dto_form_dict = public_dashboard_dto.from_dict(public_dashboard_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


