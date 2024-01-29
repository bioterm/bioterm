# QuotaDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**target** | **str** |  | [optional] 
**used** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.quota_dto import QuotaDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaDTO from a JSON string
quota_dto_instance = QuotaDTO.from_json(json)
# print the JSON string representation of the object
print QuotaDTO.to_json()

# convert the object into a dict
quota_dto_dict = quota_dto_instance.to_dict()
# create an instance of QuotaDTO from a dict
quota_dto_form_dict = quota_dto.from_dict(quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


