# TeamGroupDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.team_group_dto import TeamGroupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGroupDTO from a JSON string
team_group_dto_instance = TeamGroupDTO.from_json(json)
# print the JSON string representation of the object
print TeamGroupDTO.to_json()

# convert the object into a dict
team_group_dto_dict = team_group_dto_instance.to_dict()
# create an instance of TeamGroupDTO from a dict
team_group_dto_form_dict = team_group_dto.from_dict(team_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


