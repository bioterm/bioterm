# TeamMemberDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_module** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**permission** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 
**team_uid** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.team_member_dto import TeamMemberDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberDTO from a JSON string
team_member_dto_instance = TeamMemberDTO.from_json(json)
# print the JSON string representation of the object
print TeamMemberDTO.to_json()

# convert the object into a dict
team_member_dto_dict = team_member_dto_instance.to_dict()
# create an instance of TeamMemberDTO from a dict
team_member_dto_form_dict = team_member_dto.from_dict(team_member_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


