# AdminCreateUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.admin_create_user_response import AdminCreateUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCreateUserResponse from a JSON string
admin_create_user_response_instance = AdminCreateUserResponse.from_json(json)
# print the JSON string representation of the object
print AdminCreateUserResponse.to_json()

# convert the object into a dict
admin_create_user_response_dict = admin_create_user_response_instance.to_dict()
# create an instance of AdminCreateUserResponse from a dict
admin_create_user_response_form_dict = admin_create_user_response.from_dict(admin_create_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


