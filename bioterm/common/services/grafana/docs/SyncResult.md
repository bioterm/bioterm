# SyncResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**failed_users** | [**List[FailedUser]**](FailedUser.md) |  | [optional] 
**missing_user_ids** | **List[int]** |  | [optional] 
**started** | **datetime** |  | [optional] 
**updated_user_ids** | **List[int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.sync_result import SyncResult

# TODO update the JSON string below
json = "{}"
# create an instance of SyncResult from a JSON string
sync_result_instance = SyncResult.from_json(json)
# print the JSON string representation of the object
print SyncResult.to_json()

# convert the object into a dict
sync_result_dict = sync_result_instance.to_dict()
# create an instance of SyncResult from a dict
sync_result_form_dict = sync_result.from_dict(sync_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


