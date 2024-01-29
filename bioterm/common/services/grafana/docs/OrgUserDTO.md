# OrgUserDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** |  | [optional] 
**auth_labels** | **List[str]** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_externally_synced** | **bool** |  | [optional] 
**last_seen_at** | **datetime** |  | [optional] 
**last_seen_at_age** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.org_user_dto import OrgUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUserDTO from a JSON string
org_user_dto_instance = OrgUserDTO.from_json(json)
# print the JSON string representation of the object
print OrgUserDTO.to_json()

# convert the object into a dict
org_user_dto_dict = org_user_dto_instance.to_dict()
# create an instance of OrgUserDTO from a dict
org_user_dto_form_dict = org_user_dto.from_dict(org_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


