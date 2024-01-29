# ReceiverExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.receiver_export import ReceiverExport

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiverExport from a JSON string
receiver_export_instance = ReceiverExport.from_json(json)
# print the JSON string representation of the object
print ReceiverExport.to_json()

# convert the object into a dict
receiver_export_dict = receiver_export_instance.to_dict()
# create an instance of ReceiverExport from a dict
receiver_export_form_dict = receiver_export.from_dict(receiver_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


