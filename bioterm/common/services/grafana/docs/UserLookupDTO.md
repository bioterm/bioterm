# UserLookupDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.user_lookup_dto import UserLookupDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserLookupDTO from a JSON string
user_lookup_dto_instance = UserLookupDTO.from_json(json)
# print the JSON string representation of the object
print UserLookupDTO.to_json()

# convert the object into a dict
user_lookup_dto_dict = user_lookup_dto_instance.to_dict()
# create an instance of UserLookupDTO from a dict
user_lookup_dto_form_dict = user_lookup_dto.from_dict(user_lookup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


