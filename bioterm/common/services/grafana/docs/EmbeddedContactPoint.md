# EmbeddedContactPoint

EmbeddedContactPoint is the contact point type that is used by grafanas embedded alertmanager implementation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**name** | **str** | Name is used as grouping key in the UI. Contact points with the same name will be grouped in the UI. | [optional] 
**provenance** | **str** |  | [optional] [readonly] 
**settings** | **object** |  | 
**type** | **str** |  | 
**uid** | **str** | UID is the unique identifier of the contact point. The UID can be set by the user. | [optional] 

## Example

```python
from grafanaApiClient.models.embedded_contact_point import EmbeddedContactPoint

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedContactPoint from a JSON string
embedded_contact_point_instance = EmbeddedContactPoint.from_json(json)
# print the JSON string representation of the object
print EmbeddedContactPoint.to_json()

# convert the object into a dict
embedded_contact_point_dict = embedded_contact_point_instance.to_dict()
# create an instance of EmbeddedContactPoint from a dict
embedded_contact_point_form_dict = embedded_contact_point.from_dict(embedded_contact_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


