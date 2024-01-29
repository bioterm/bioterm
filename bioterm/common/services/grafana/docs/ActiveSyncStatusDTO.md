# ActiveSyncStatusDTO

ActiveSyncStatusDTO holds the information for LDAP background Sync

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**next_sync** | **datetime** |  | [optional] 
**prev_sync** | [**SyncResult**](SyncResult.md) |  | [optional] 
**schedule** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.active_sync_status_dto import ActiveSyncStatusDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveSyncStatusDTO from a JSON string
active_sync_status_dto_instance = ActiveSyncStatusDTO.from_json(json)
# print the JSON string representation of the object
print ActiveSyncStatusDTO.to_json()

# convert the object into a dict
active_sync_status_dto_dict = active_sync_status_dto_instance.to_dict()
# create an instance of ActiveSyncStatusDTO from a dict
active_sync_status_dto_form_dict = active_sync_status_dto.from_dict(active_sync_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


