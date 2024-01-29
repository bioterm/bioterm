# UpdateServiceAccountForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_disabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**service_account_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_service_account_form import UpdateServiceAccountForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceAccountForm from a JSON string
update_service_account_form_instance = UpdateServiceAccountForm.from_json(json)
# print the JSON string representation of the object
print UpdateServiceAccountForm.to_json()

# convert the object into a dict
update_service_account_form_dict = update_service_account_form_instance.to_dict()
# create an instance of UpdateServiceAccountForm from a dict
update_service_account_form_form_dict = update_service_account_form.from_dict(update_service_account_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


