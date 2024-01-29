# Extension

Extension represents the ASN.1 structure of the same name. See RFC 5280, section 4.2.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **bool** |  | [optional] 
**id** | **List[int]** |  | [optional] 
**value** | **List[int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.extension import Extension

# TODO update the JSON string below
json = "{}"
# create an instance of Extension from a JSON string
extension_instance = Extension.from_json(json)
# print the JSON string representation of the object
print Extension.to_json()

# convert the object into a dict
extension_dict = extension_instance.to_dict()
# create an instance of Extension from a dict
extension_form_dict = extension.from_dict(extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


