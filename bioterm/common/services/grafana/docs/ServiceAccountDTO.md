# ServiceAccountDTO

swagger: model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**is_external** | **bool** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**tokens** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.service_account_dto import ServiceAccountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAccountDTO from a JSON string
service_account_dto_instance = ServiceAccountDTO.from_json(json)
# print the JSON string representation of the object
print ServiceAccountDTO.to_json()

# convert the object into a dict
service_account_dto_dict = service_account_dto_instance.to_dict()
# create an instance of ServiceAccountDTO from a dict
service_account_dto_form_dict = service_account_dto.from_dict(service_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


