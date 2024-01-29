# PostAnnotationsCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **int** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | 
**time** | **int** |  | [optional] 
**time_end** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.post_annotations_cmd import PostAnnotationsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnnotationsCmd from a JSON string
post_annotations_cmd_instance = PostAnnotationsCmd.from_json(json)
# print the JSON string representation of the object
print PostAnnotationsCmd.to_json()

# convert the object into a dict
post_annotations_cmd_dict = post_annotations_cmd_instance.to_dict()
# create an instance of PostAnnotationsCmd from a dict
post_annotations_cmd_form_dict = post_annotations_cmd.from_dict(post_annotations_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


