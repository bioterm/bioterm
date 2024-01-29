# DashboardMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations_permissions** | [**AnnotationPermission**](AnnotationPermission.md) |  | [optional] 
**can_admin** | **bool** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**can_edit** | **bool** |  | [optional] 
**can_save** | **bool** |  | [optional] 
**can_star** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_title** | **str** |  | [optional] 
**folder_uid** | **str** |  | [optional] 
**folder_url** | **str** |  | [optional] 
**has_acl** | **bool** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**is_snapshot** | **bool** |  | [optional] 
**is_starred** | **bool** |  | [optional] 
**provisioned** | **bool** |  | [optional] 
**provisioned_external_id** | **str** |  | [optional] 
**public_dashboard_enabled** | **bool** |  | [optional] 
**public_dashboard_uid** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_meta import DashboardMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMeta from a JSON string
dashboard_meta_instance = DashboardMeta.from_json(json)
# print the JSON string representation of the object
print DashboardMeta.to_json()

# convert the object into a dict
dashboard_meta_dict = dashboard_meta_instance.to_dict()
# create an instance of DashboardMeta from a dict
dashboard_meta_form_dict = dashboard_meta.from_dict(dashboard_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


