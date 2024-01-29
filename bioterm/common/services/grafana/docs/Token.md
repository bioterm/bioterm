# Token


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**details_url** | **str** |  | [optional] 
**exp** | **int** |  | [optional] 
**iat** | **int** |  | [optional] 
**included_users** | **int** |  | [optional] 
**iss** | **str** |  | [optional] 
**jti** | **str** |  | [optional] 
**lexp** | **int** |  | [optional] 
**lic_exp_warn_days** | **int** |  | [optional] 
**lid** | **str** |  | [optional] 
**limit_by** | **str** |  | [optional] 
**max_concurrent_user_sessions** | **int** |  | [optional] 
**nbf** | **int** |  | [optional] 
**prod** | **List[str]** |  | [optional] 
**slug** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**sub** | **str** |  | [optional] 
**tok_exp_warn_days** | **int** |  | [optional] 
**trial** | **bool** |  | [optional] 
**trial_exp** | **int** |  | [optional] 
**update_days** | **int** |  | [optional] 
**usage_billing** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print Token.to_json()

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_form_dict = token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


