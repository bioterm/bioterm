# DashboardSnapshotDTO

DashboardSnapshotDTO without dashboard map

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**external** | **bool** |  | [optional] 
**external_url** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_snapshot_dto import DashboardSnapshotDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSnapshotDTO from a JSON string
dashboard_snapshot_dto_instance = DashboardSnapshotDTO.from_json(json)
# print the JSON string representation of the object
print DashboardSnapshotDTO.to_json()

# convert the object into a dict
dashboard_snapshot_dto_dict = dashboard_snapshot_dto_instance.to_dict()
# create an instance of DashboardSnapshotDTO from a dict
dashboard_snapshot_dto_form_dict = dashboard_snapshot_dto.from_dict(dashboard_snapshot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


