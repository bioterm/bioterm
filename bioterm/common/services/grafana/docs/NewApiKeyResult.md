# NewApiKeyResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.new_api_key_result import NewApiKeyResult

# TODO update the JSON string below
json = "{}"
# create an instance of NewApiKeyResult from a JSON string
new_api_key_result_instance = NewApiKeyResult.from_json(json)
# print the JSON string representation of the object
print NewApiKeyResult.to_json()

# convert the object into a dict
new_api_key_result_dict = new_api_key_result_instance.to_dict()
# create an instance of NewApiKeyResult from a dict
new_api_key_result_form_dict = new_api_key_result.from_dict(new_api_key_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


