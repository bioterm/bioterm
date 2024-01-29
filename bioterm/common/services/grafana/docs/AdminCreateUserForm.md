# AdminCreateUserForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.admin_create_user_form import AdminCreateUserForm

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCreateUserForm from a JSON string
admin_create_user_form_instance = AdminCreateUserForm.from_json(json)
# print the JSON string representation of the object
print AdminCreateUserForm.to_json()

# convert the object into a dict
admin_create_user_form_dict = admin_create_user_form_instance.to_dict()
# create an instance of AdminCreateUserForm from a dict
admin_create_user_form_form_dict = admin_create_user_form.from_dict(admin_create_user_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


