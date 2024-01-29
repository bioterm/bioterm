# FrameMeta

https://github.com/grafana/grafana/blob/master/packages/grafana-data/src/types/data.ts#L11 NOTE -- in javascript this can accept any `[key: string]: any;` however this interface only exposes the values we want to be exposed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel is the path to a stream in grafana live that has real-time updates for this data. | [optional] 
**custom** | **object** | Custom datasource specific values. | [optional] 
**data_topic** | **str** | nolint:revive | [optional] 
**executed_query_string** | **str** | ExecutedQueryString is the raw query sent to the underlying system. All macros and templating have been applied.  When metadata contains this value, it will be shown in the query inspector. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | Notices provide additional information about the data in the Frame that Grafana can display to the user in the user interface. | [optional] 
**path** | **str** | Path is a browsable path on the datasource. | [optional] 
**path_separator** | **str** | PathSeparator defines the separator pattern to decode a hierarchy. The default separator is &#39;/&#39;. | [optional] 
**preferred_visualisation_plugin_id** | **str** | PreferredVisualizationPluginId sets the panel plugin id to use to render the data when using Explore. If the plugin cannot be found will fall back to PreferredVisualization. | [optional] 
**preferred_visualisation_type** | **str** |  | [optional] 
**stats** | [**List[QueryStat]**](QueryStat.md) | Stats is an array of query result statistics. | [optional] 
**type** | **str** | A FrameType string, when present in a frame&#39;s metadata, asserts that the frame&#39;s structure conforms to the FrameType&#39;s specification. This property is currently optional, so FrameType may be FrameTypeUnknown even if the properties of the Frame correspond to a defined FrameType. | [optional] 
**type_version** | **List[int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.frame_meta import FrameMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FrameMeta from a JSON string
frame_meta_instance = FrameMeta.from_json(json)
# print the JSON string representation of the object
print FrameMeta.to_json()

# convert the object into a dict
frame_meta_dict = frame_meta_instance.to_dict()
# create an instance of FrameMeta from a dict
frame_meta_form_dict = frame_meta.from_dict(frame_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


