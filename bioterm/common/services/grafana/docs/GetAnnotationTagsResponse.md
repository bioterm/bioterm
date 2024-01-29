# GetAnnotationTagsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**FindTagsResult**](FindTagsResult.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.get_annotation_tags_response import GetAnnotationTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnnotationTagsResponse from a JSON string
get_annotation_tags_response_instance = GetAnnotationTagsResponse.from_json(json)
# print the JSON string representation of the object
print GetAnnotationTagsResponse.to_json()

# convert the object into a dict
get_annotation_tags_response_dict = get_annotation_tags_response_instance.to_dict()
# create an instance of GetAnnotationTagsResponse from a dict
get_annotation_tags_response_form_dict = get_annotation_tags_response.from_dict(get_annotation_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


