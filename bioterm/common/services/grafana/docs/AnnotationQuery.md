# AnnotationQuery

TODO docs FROM: AnnotationQuery in grafana-data/src/types/annotations.ts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**built_in** | **float** | Set to 1 for the standard annotation query all dashboards have by default. | [optional] 
**datasource** | [**DataSourceRef**](DataSourceRef.md) |  | [optional] 
**enable** | **bool** | When enabled the annotation query is issued with every dashboard refresh | [optional] 
**filter** | [**AnnotationPanelFilter**](AnnotationPanelFilter.md) |  | [optional] 
**hide** | **bool** | Annotation queries can be toggled on or off at the top of the dashboard. When hide is true, the toggle is not shown in the dashboard. | [optional] 
**icon_color** | **str** | Color to use for the annotation event markers | [optional] 
**name** | **str** | Name of annotation. | [optional] 
**target** | [**AnnotationTarget**](AnnotationTarget.md) |  | [optional] 
**type** | **str** | TODO -- this should not exist here, it is based on the --grafana-- datasource | [optional] 

## Example

```python
from grafanaApiClient.models.annotation_query import AnnotationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationQuery from a JSON string
annotation_query_instance = AnnotationQuery.from_json(json)
# print the JSON string representation of the object
print AnnotationQuery.to_json()

# convert the object into a dict
annotation_query_dict = annotation_query_instance.to_dict()
# create an instance of AnnotationQuery from a dict
annotation_query_form_dict = annotation_query.from_dict(annotation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


