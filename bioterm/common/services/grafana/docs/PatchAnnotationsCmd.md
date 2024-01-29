# PatchAnnotationsCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_end** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.patch_annotations_cmd import PatchAnnotationsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAnnotationsCmd from a JSON string
patch_annotations_cmd_instance = PatchAnnotationsCmd.from_json(json)
# print the JSON string representation of the object
print PatchAnnotationsCmd.to_json()

# convert the object into a dict
patch_annotations_cmd_dict = patch_annotations_cmd_instance.to_dict()
# create an instance of PatchAnnotationsCmd from a dict
patch_annotations_cmd_form_dict = patch_annotations_cmd.from_dict(patch_annotations_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


