# OrgDetailsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.org_details_dto import OrgDetailsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrgDetailsDTO from a JSON string
org_details_dto_instance = OrgDetailsDTO.from_json(json)
# print the JSON string representation of the object
print OrgDetailsDTO.to_json()

# convert the object into a dict
org_details_dto_dict = org_details_dto_instance.to_dict()
# create an instance of OrgDetailsDTO from a dict
org_details_dto_form_dict = org_details_dto.from_dict(org_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


