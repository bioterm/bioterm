# AdminUpdateUserPermissionsForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_grafana_admin** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.admin_update_user_permissions_form import AdminUpdateUserPermissionsForm

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUpdateUserPermissionsForm from a JSON string
admin_update_user_permissions_form_instance = AdminUpdateUserPermissionsForm.from_json(json)
# print the JSON string representation of the object
print AdminUpdateUserPermissionsForm.to_json()

# convert the object into a dict
admin_update_user_permissions_form_dict = admin_update_user_permissions_form_instance.to_dict()
# create an instance of AdminUpdateUserPermissionsForm from a dict
admin_update_user_permissions_form_form_dict = admin_update_user_permissions_form.from_dict(admin_update_user_permissions_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


