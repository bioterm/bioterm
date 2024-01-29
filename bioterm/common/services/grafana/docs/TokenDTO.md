# TokenDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**expiration** | **datetime** |  | [optional] 
**has_expired** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**is_revoked** | **bool** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**seconds_until_expiration** | **float** |  | [optional] 

## Example

```python
from grafanaApiClient.models.token_dto import TokenDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDTO from a JSON string
token_dto_instance = TokenDTO.from_json(json)
# print the JSON string representation of the object
print TokenDTO.to_json()

# convert the object into a dict
token_dto_dict = token_dto_instance.to_dict()
# create an instance of TokenDTO from a dict
token_dto_form_dict = token_dto.from_dict(token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


