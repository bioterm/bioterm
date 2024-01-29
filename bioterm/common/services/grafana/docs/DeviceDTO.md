# DeviceDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**device_id** | **str** |  | [optional] 
**last_seen_at** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.device_dto import DeviceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDTO from a JSON string
device_dto_instance = DeviceDTO.from_json(json)
# print the JSON string representation of the object
print DeviceDTO.to_json()

# convert the object into a dict
device_dto_dict = device_dto_instance.to_dict()
# create an instance of DeviceDTO from a dict
device_dto_form_dict = device_dto.from_dict(device_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


