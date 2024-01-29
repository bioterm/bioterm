# AnnotationPermission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**AnnotationActions**](AnnotationActions.md) |  | [optional] 
**organization** | [**AnnotationActions**](AnnotationActions.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_permission import AnnotationPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationPermission from a JSON string
annotation_permission_instance = AnnotationPermission.from_json(json)
# print the JSON string representation of the object
print AnnotationPermission.to_json()

# convert the object into a dict
annotation_permission_dict = annotation_permission_instance.to_dict()
# create an instance of AnnotationPermission from a dict
annotation_permission_form_dict = annotation_permission.from_dict(annotation_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


