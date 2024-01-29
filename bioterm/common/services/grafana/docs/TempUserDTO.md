# TempUserDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**email_sent** | **bool** |  | [optional] 
**email_sent_on** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**invited_by_email** | **str** |  | [optional] 
**invited_by_login** | **str** |  | [optional] 
**invited_by_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.temp_user_dto import TempUserDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TempUserDTO from a JSON string
temp_user_dto_instance = TempUserDTO.from_json(json)
# print the JSON string representation of the object
print TempUserDTO.to_json()

# convert the object into a dict
temp_user_dto_dict = temp_user_dto_instance.to_dict()
# create an instance of TempUserDTO from a dict
temp_user_dto_form_dict = temp_user_dto.from_dict(temp_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


