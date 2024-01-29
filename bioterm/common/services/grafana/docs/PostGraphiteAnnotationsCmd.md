# PostGraphiteAnnotationsCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 
**what** | **str** |  | [optional] 
**when** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.post_graphite_annotations_cmd import PostGraphiteAnnotationsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of PostGraphiteAnnotationsCmd from a JSON string
post_graphite_annotations_cmd_instance = PostGraphiteAnnotationsCmd.from_json(json)
# print the JSON string representation of the object
print PostGraphiteAnnotationsCmd.to_json()

# convert the object into a dict
post_graphite_annotations_cmd_dict = post_graphite_annotations_cmd_instance.to_dict()
# create an instance of PostGraphiteAnnotationsCmd from a dict
post_graphite_annotations_cmd_form_dict = post_graphite_annotations_cmd.from_dict(post_graphite_annotations_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


