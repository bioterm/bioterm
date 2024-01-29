# FindTagsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[TagsDTO]**](TagsDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.find_tags_result import FindTagsResult

# TODO update the JSON string below
json = "{}"
# create an instance of FindTagsResult from a JSON string
find_tags_result_instance = FindTagsResult.from_json(json)
# print the JSON string representation of the object
print FindTagsResult.to_json()

# convert the object into a dict
find_tags_result_dict = find_tags_result_instance.to_dict()
# create an instance of FindTagsResult from a dict
find_tags_result_form_dict = find_tags_result.from_dict(find_tags_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


