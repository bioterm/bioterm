# AnnotationEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**is_region** | **bool** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**source** | [**AnnotationQuery**](AnnotationQuery.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_end** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_event import AnnotationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationEvent from a JSON string
annotation_event_instance = AnnotationEvent.from_json(json)
# print the JSON string representation of the object
print AnnotationEvent.to_json()

# convert the object into a dict
annotation_event_dict = annotation_event_instance.to_dict()
# create an instance of AnnotationEvent from a dict
annotation_event_form_dict = annotation_event.from_dict(annotation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


