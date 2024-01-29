# AnnotationPanelFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **bool** | Should the specified panels be included or excluded | [optional] 
**ids** | **List[int]** | Panel IDs that should be included or excluded | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_panel_filter import AnnotationPanelFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPanelFilter from a JSON string
annotation_panel_filter_instance = AnnotationPanelFilter.from_json(json)
# print the JSON string representation of the object
print AnnotationPanelFilter.to_json()

# convert the object into a dict
annotation_panel_filter_dict = annotation_panel_filter_instance.to_dict()
# create an instance of AnnotationPanelFilter from a dict
annotation_panel_filter_form_dict = annotation_panel_filter.from_dict(annotation_panel_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


