# ApiKeyDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** | Metadata contains user accesses for a given resource Ex: map[string]bool{\&quot;create\&quot;:true, \&quot;delete\&quot;: true} | [optional] 
**expiration** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**last_used_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.api_key_dto import ApiKeyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyDTO from a JSON string
api_key_dto_instance = ApiKeyDTO.from_json(json)
# print the JSON string representation of the object
print ApiKeyDTO.to_json()

# convert the object into a dict
api_key_dto_dict = api_key_dto_instance.to_dict()
# create an instance of ApiKeyDTO from a dict
api_key_dto_form_dict = api_key_dto.from_dict(api_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


