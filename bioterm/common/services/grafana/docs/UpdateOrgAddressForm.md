# UpdateOrgAddressForm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_org_address_form import UpdateOrgAddressForm

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgAddressForm from a JSON string
update_org_address_form_instance = UpdateOrgAddressForm.from_json(json)
# print the JSON string representation of the object
print UpdateOrgAddressForm.to_json()

# convert the object into a dict
update_org_address_form_dict = update_org_address_form_instance.to_dict()
# create an instance of UpdateOrgAddressForm from a dict
update_org_address_form_form_dict = update_org_address_form.from_dict(update_org_address_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


