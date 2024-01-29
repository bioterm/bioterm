# AnnotationTarget

TODO: this should be a regular DataQuery that depends on the selected dashboard these match the properties of the \"grafana\" datasouce that is default in most dashboards

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Only required/valid for the grafana datasource... but code+tests is already depending on it so hard to change | [optional] 
**match_any** | **bool** | Only required/valid for the grafana datasource... but code+tests is already depending on it so hard to change | [optional] 
**tags** | **List[str]** | Only required/valid for the grafana datasource... but code+tests is already depending on it so hard to change | [optional] 
**type** | **str** | Only required/valid for the grafana datasource... but code+tests is already depending on it so hard to change | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_target import AnnotationTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationTarget from a JSON string
annotation_target_instance = AnnotationTarget.from_json(json)
# print the JSON string representation of the object
print AnnotationTarget.to_json()

# convert the object into a dict
annotation_target_dict = annotation_target_instance.to_dict()
# create an instance of AnnotationTarget from a dict
annotation_target_form_dict = annotation_target.from_dict(annotation_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


