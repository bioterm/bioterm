# OrgDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.org_dto import OrgDTO

# TODO update the JSON string below
json = "{}"
# create an instance of OrgDTO from a JSON string
org_dto_instance = OrgDTO.from_json(json)
# print the JSON string representation of the object
print OrgDTO.to_json()

# convert the object into a dict
org_dto_dict = org_dto_instance.to_dict()
# create an instance of OrgDTO from a dict
org_dto_form_dict = org_dto.from_dict(org_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


