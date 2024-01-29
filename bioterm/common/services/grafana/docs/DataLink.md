# DataLink

DataLink define what

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal** | [**InternalDataLink**](InternalDataLink.md) |  | [optional] 
**target_blank** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.data_link import DataLink

# TODO update the JSON string below
json = "{}"
# create an instance of DataLink from a JSON string
data_link_instance = DataLink.from_json(json)
# print the JSON string representation of the object
print DataLink.to_json()

# convert the object into a dict
data_link_dict = data_link_instance.to_dict()
# create an instance of DataLink from a dict
data_link_form_dict = data_link.from_dict(data_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


