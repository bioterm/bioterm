# MassDeleteAnnotationsCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation_id** | **int** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**panel_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.mass_delete_annotations_cmd import MassDeleteAnnotationsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of MassDeleteAnnotationsCmd from a JSON string
mass_delete_annotations_cmd_instance = MassDeleteAnnotationsCmd.from_json(json)
# print the JSON string representation of the object
print MassDeleteAnnotationsCmd.to_json()

# convert the object into a dict
mass_delete_annotations_cmd_dict = mass_delete_annotations_cmd_instance.to_dict()
# create an instance of MassDeleteAnnotationsCmd from a dict
mass_delete_annotations_cmd_form_dict = mass_delete_annotations_cmd.from_dict(mass_delete_annotations_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


