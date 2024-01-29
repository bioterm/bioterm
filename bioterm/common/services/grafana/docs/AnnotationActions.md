# AnnotationActions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_add** | **bool** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**can_edit** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_actions import AnnotationActions

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationActions from a JSON string
annotation_actions_instance = AnnotationActions.from_json(json)
# print the JSON string representation of the object
print AnnotationActions.to_json()

# convert the object into a dict
annotation_actions_dict = annotation_actions_instance.to_dict()
# create an instance of AnnotationActions from a dict
annotation_actions_form_dict = annotation_actions.from_dict(annotation_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


