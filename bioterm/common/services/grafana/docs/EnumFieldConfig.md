# EnumFieldConfig

Enum field config Vector values are used as lookup keys into the enum fields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **List[str]** | Color is the color value for a given index (empty is undefined) | [optional] 
**description** | **List[str]** | Description of the enum state | [optional] 
**icon** | **List[str]** | Icon supports setting an icon for a given index value | [optional] 
**text** | **List[str]** | Value is the string display value for a given index | [optional] 

## Example

```python
from grafanaApiClient.models.enum_field_config import EnumFieldConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EnumFieldConfig from a JSON string
enum_field_config_instance = EnumFieldConfig.from_json(json)
# print the JSON string representation of the object
print EnumFieldConfig.to_json()

# convert the object into a dict
enum_field_config_dict = enum_field_config_instance.to_dict()
# create an instance of EnumFieldConfig from a dict
enum_field_config_form_dict = enum_field_config.from_dict(enum_field_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


