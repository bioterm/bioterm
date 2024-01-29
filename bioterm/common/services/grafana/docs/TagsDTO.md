# TagsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.tags_dto import TagsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TagsDTO from a JSON string
tags_dto_instance = TagsDTO.from_json(json)
# print the JSON string representation of the object
print TagsDTO.to_json()

# convert the object into a dict
tags_dto_dict = tags_dto_instance.to_dict()
# create an instance of TagsDTO from a dict
tags_dto_form_dict = tags_dto.from_dict(tags_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


