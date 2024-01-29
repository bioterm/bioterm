# CreateRoleForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**var_global** | **bool** |  | [optional] 
**group** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 
**uid** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_role_form import CreateRoleForm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleForm from a JSON string
create_role_form_instance = CreateRoleForm.from_json(json)
# print the JSON string representation of the object
print CreateRoleForm.to_json()

# convert the object into a dict
create_role_form_dict = create_role_form_instance.to_dict()
# create an instance of CreateRoleForm from a dict
create_role_form_form_dict = create_role_form.from_dict(create_role_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


