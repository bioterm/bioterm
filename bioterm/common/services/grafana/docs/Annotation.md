# Annotation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | [optional] 
**alert_name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**created** | **int** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**login** | **str** |  | [optional] 
**new_state** | **str** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**prev_state** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 
**time** | **int** |  | [optional] 
**time_end** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.annotation import Annotation

# TODO update the JSON string below
json = "{}"
# create an instance of Annotation from a JSON string
annotation_instance = Annotation.from_json(json)
# print the JSON string representation of the object
print Annotation.to_json()

# convert the object into a dict
annotation_dict = annotation_instance.to_dict()
# create an instance of Annotation from a dict
annotation_form_dict = annotation.from_dict(annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


