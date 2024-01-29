# TeamDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**permission** | **int** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.team_dto import TeamDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDTO from a JSON string
team_dto_instance = TeamDTO.from_json(json)
# print the JSON string representation of the object
print TeamDTO.to_json()

# convert the object into a dict
team_dto_dict = team_dto_instance.to_dict()
# create an instance of TeamDTO from a dict
team_dto_form_dict = team_dto.from_dict(team_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


