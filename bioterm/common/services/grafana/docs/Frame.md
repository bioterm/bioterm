# Frame

Each Field is well typed by its FieldType and supports optional Labels.  A Frame is a general data container for Grafana. A Frame can be table data or time series data depending on its content and field types.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[Field]**](Field.md) | Fields are the columns of a frame. All Fields must be of the same the length when marshalling the Frame for transmission. There should be no &#x60;nil&#x60; entries in the Fields slice (making them pointers was a mistake). | [optional] 
**meta** | [**FrameMeta**](FrameMeta.md) |  | [optional] 
**name** | **str** | Name is used in some Grafana visualizations. | [optional] 
**ref_id** | **str** | RefID is a property that can be set to match a Frame to its originating query. | [optional] 

## Example

```python
from grafanaApiClient.models.frame import Frame

# TODO update the JSON string below
json = "{}"
# create an instance of Frame from a JSON string
frame_instance = Frame.from_json(json)
# print the JSON string representation of the object
print Frame.to_json()

# convert the object into a dict
frame_dict = frame_instance.to_dict()
# create an instance of Frame from a dict
frame_form_dict = frame.from_dict(frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


