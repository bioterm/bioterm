# UserOrgDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.user_org_dto import UserOrgDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrgDTO from a JSON string
user_org_dto_instance = UserOrgDTO.from_json(json)
# print the JSON string representation of the object
print UserOrgDTO.to_json()

# convert the object into a dict
user_org_dto_dict = user_org_dto_instance.to_dict()
# create an instance of UserOrgDTO from a dict
user_org_dto_form_dict = user_org_dto.from_dict(user_org_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


