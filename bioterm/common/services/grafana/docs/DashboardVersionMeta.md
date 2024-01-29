# DashboardVersionMeta

DashboardVersionMeta extends the DashboardVersionDTO with the names associated with the UserIds, overriding the field with the same name from the DashboardVersionDTO model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**parent_version** | **int** |  | [optional] 
**restored_from** | **int** |  | [optional] 
**uid** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_version_meta import DashboardVersionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardVersionMeta from a JSON string
dashboard_version_meta_instance = DashboardVersionMeta.from_json(json)
# print the JSON string representation of the object
print DashboardVersionMeta.to_json()

# convert the object into a dict
dashboard_version_meta_dict = dashboard_version_meta_instance.to_dict()
# create an instance of DashboardVersionMeta from a dict
dashboard_version_meta_form_dict = dashboard_version_meta.from_dict(dashboard_version_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


