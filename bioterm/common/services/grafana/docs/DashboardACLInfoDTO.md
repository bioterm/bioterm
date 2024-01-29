# DashboardACLInfoDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** |  | [optional] 
**inherited** | **bool** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**permission** | **int** |  | [optional] 
**permission_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**team** | **str** |  | [optional] 
**team_avatar_url** | **str** |  | [optional] 
**team_email** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**user_avatar_url** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_login** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_acl_info_dto import DashboardACLInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardACLInfoDTO from a JSON string
dashboard_acl_info_dto_instance = DashboardACLInfoDTO.from_json(json)
# print the JSON string representation of the object
print DashboardACLInfoDTO.to_json()

# convert the object into a dict
dashboard_acl_info_dto_dict = dashboard_acl_info_dto_instance.to_dict()
# create an instance of DashboardACLInfoDTO from a dict
dashboard_acl_info_dto_form_dict = dashboard_acl_info_dto.from_dict(dashboard_acl_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


