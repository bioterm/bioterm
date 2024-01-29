# AddInviteForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_or_email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**send_email** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_invite_form import AddInviteForm

# TODO update the JSON string below
json = "{}"
# create an instance of AddInviteForm from a JSON string
add_invite_form_instance = AddInviteForm.from_json(json)
# print the JSON string representation of the object
print AddInviteForm.to_json()

# convert the object into a dict
add_invite_form_dict = add_invite_form_instance.to_dict()
# create an instance of AddInviteForm from a dict
add_invite_form_form_dict = add_invite_form.from_dict(add_invite_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


