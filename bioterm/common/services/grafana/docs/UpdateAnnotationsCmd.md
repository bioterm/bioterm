# UpdateAnnotationsCmd


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
from grafanaApiClient.models.update_annotations_cmd import UpdateAnnotationsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnnotationsCmd from a JSON string
update_annotations_cmd_instance = UpdateAnnotationsCmd.from_json(json)
# print the JSON string representation of the object
print UpdateAnnotationsCmd.to_json()

# convert the object into a dict
update_annotations_cmd_dict = update_annotations_cmd_instance.to_dict()
# create an instance of UpdateAnnotationsCmd from a dict
update_annotations_cmd_form_dict = update_annotations_cmd.from_dict(update_annotations_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


