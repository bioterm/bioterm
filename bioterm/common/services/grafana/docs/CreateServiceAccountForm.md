# CreateServiceAccountForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_disabled** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_service_account_form import CreateServiceAccountForm

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceAccountForm from a JSON string
create_service_account_form_instance = CreateServiceAccountForm.from_json(json)
# print the JSON string representation of the object
print CreateServiceAccountForm.to_json()

# convert the object into a dict
create_service_account_form_dict = create_service_account_form_instance.to_dict()
# create an instance of CreateServiceAccountForm from a dict
create_service_account_form_form_dict = create_service_account_form.from_dict(create_service_account_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


