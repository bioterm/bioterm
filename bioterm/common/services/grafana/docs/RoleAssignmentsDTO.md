# RoleAssignmentsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_uid** | **str** |  | [optional] 
**service_accounts** | **List[int]** |  | [optional] 
**teams** | **List[int]** |  | [optional] 
**users** | **List[int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.role_assignments_dto import RoleAssignmentsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignmentsDTO from a JSON string
role_assignments_dto_instance = RoleAssignmentsDTO.from_json(json)
# print the JSON string representation of the object
print RoleAssignmentsDTO.to_json()

# convert the object into a dict
role_assignments_dto_dict = role_assignments_dto_instance.to_dict()
# create an instance of RoleAssignmentsDTO from a dict
role_assignments_dto_form_dict = role_assignments_dto.from_dict(role_assignments_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


