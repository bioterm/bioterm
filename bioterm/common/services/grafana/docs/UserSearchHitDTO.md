# UserSearchHitDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_labels** | **List[str]** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**last_seen_at** | **datetime** |  | [optional] 
**last_seen_at_age** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.user_search_hit_dto import UserSearchHitDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchHitDTO from a JSON string
user_search_hit_dto_instance = UserSearchHitDTO.from_json(json)
# print the JSON string representation of the object
print UserSearchHitDTO.to_json()

# convert the object into a dict
user_search_hit_dto_dict = user_search_hit_dto_instance.to_dict()
# create an instance of UserSearchHitDTO from a dict
user_search_hit_dto_form_dict = user_search_hit_dto.from_dict(user_search_hit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


