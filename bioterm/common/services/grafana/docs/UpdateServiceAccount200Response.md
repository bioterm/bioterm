# UpdateServiceAccount200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**serviceaccount** | [**ServiceAccountProfileDTO**](ServiceAccountProfileDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_service_account200_response import UpdateServiceAccount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceAccount200Response from a JSON string
update_service_account200_response_instance = UpdateServiceAccount200Response.from_json(json)
# print the JSON string representation of the object
print UpdateServiceAccount200Response.to_json()

# convert the object into a dict
update_service_account200_response_dict = update_service_account200_response_instance.to_dict()
# create an instance of UpdateServiceAccount200Response from a dict
update_service_account200_response_form_dict = update_service_account200_response.from_dict(update_service_account200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


