# FieldTypeConfig

FieldTypeConfig has type specific configs, only one should be active at a time

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum** | [**EnumFieldConfig**](EnumFieldConfig.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.field_type_config import FieldTypeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FieldTypeConfig from a JSON string
field_type_config_instance = FieldTypeConfig.from_json(json)
# print the JSON string representation of the object
print FieldTypeConfig.to_json()

# convert the object into a dict
field_type_config_dict = field_type_config_instance.to_dict()
# create an instance of FieldTypeConfig from a dict
field_type_config_form_dict = field_type_config.from_dict(field_type_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


