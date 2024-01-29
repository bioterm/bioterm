# InternalDataLink

InternalDataLink definition to allow Explore links to be constructed in the backend

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_name** | **str** |  | [optional] 
**datasource_uid** | **str** |  | [optional] 
**panels_state** | **object** | This is an object constructed with the keys as the values of the enum VisType and the value being a bag of properties | [optional] 
**query** | **object** |  | [optional] 
**time_range** | [**TimeRange**](TimeRange.md) |  | [optional] 
**transformations** | [**List[LinkTransformationConfig]**](LinkTransformationConfig.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.internal_data_link import InternalDataLink

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDataLink from a JSON string
internal_data_link_instance = InternalDataLink.from_json(json)
# print the JSON string representation of the object
print InternalDataLink.to_json()

# convert the object into a dict
internal_data_link_dict = internal_data_link_instance.to_dict()
# create an instance of InternalDataLink from a dict
internal_data_link_form_dict = internal_data_link.from_dict(internal_data_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


