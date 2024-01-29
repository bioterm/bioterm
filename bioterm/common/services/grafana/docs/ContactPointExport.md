# ContactPointExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**receivers** | [**List[ReceiverExport]**](ReceiverExport.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.contact_point_export import ContactPointExport

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPointExport from a JSON string
contact_point_export_instance = ContactPointExport.from_json(json)
# print the JSON string representation of the object
print ContactPointExport.to_json()

# convert the object into a dict
contact_point_export_dict = contact_point_export_instance.to_dict()
# create an instance of ContactPointExport from a dict
contact_point_export_form_dict = contact_point_export.from_dict(contact_point_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


