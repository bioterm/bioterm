# DataSourceRef

Ref to a DataSource instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The plugin type-id | [optional] 
**uid** | **str** | Specific datasource instance | [optional] 

## Example

```python
from grafanaApiClient.models.data_source_ref import DataSourceRef

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceRef from a JSON string
data_source_ref_instance = DataSourceRef.from_json(json)
# print the JSON string representation of the object
print DataSourceRef.to_json()

# convert the object into a dict
data_source_ref_dict = data_source_ref_instance.to_dict()
# create an instance of DataSourceRef from a dict
data_source_ref_form_dict = data_source_ref.from_dict(data_source_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


