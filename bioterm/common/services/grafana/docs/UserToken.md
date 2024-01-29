# UserToken

UserToken represents a user token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | [optional] 
**auth_token_seen** | **bool** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**prev_auth_token** | **str** |  | [optional] 
**revoked_at** | **int** |  | [optional] 
**rotated_at** | **int** |  | [optional] 
**seen_at** | **int** |  | [optional] 
**unhashed_token** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.user_token import UserToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserToken from a JSON string
user_token_instance = UserToken.from_json(json)
# print the JSON string representation of the object
print UserToken.to_json()

# convert the object into a dict
user_token_dict = user_token_instance.to_dict()
# create an instance of UserToken from a dict
user_token_form_dict = user_token.from_dict(user_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


