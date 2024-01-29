# UserProfileDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** |  | [optional] 
**auth_labels** | **List[str]** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_external** | **bool** |  | [optional] 
**is_externally_synced** | **bool** |  | [optional] 
**is_grafana_admin** | **bool** |  | [optional] 
**is_grafana_admin_externally_synced** | **bool** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**theme** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.user_profile_dto import UserProfileDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileDTO from a JSON string
user_profile_dto_instance = UserProfileDTO.from_json(json)
# print the JSON string representation of the object
print UserProfileDTO.to_json()

# convert the object into a dict
user_profile_dto_dict = user_profile_dto_instance.to_dict()
# create an instance of UserProfileDTO from a dict
user_profile_dto_form_dict = user_profile_dto.from_dict(user_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


