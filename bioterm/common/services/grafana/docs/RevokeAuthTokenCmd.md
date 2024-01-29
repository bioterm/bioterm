# RevokeAuthTokenCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.revoke_auth_token_cmd import RevokeAuthTokenCmd

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAuthTokenCmd from a JSON string
revoke_auth_token_cmd_instance = RevokeAuthTokenCmd.from_json(json)
# print the JSON string representation of the object
print RevokeAuthTokenCmd.to_json()

# convert the object into a dict
revoke_auth_token_cmd_dict = revoke_auth_token_cmd_instance.to_dict()
# create an instance of RevokeAuthTokenCmd from a dict
revoke_auth_token_cmd_form_dict = revoke_auth_token_cmd.from_dict(revoke_auth_token_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


