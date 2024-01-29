# DashboardACLUpdateItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_acl_update_item import DashboardACLUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardACLUpdateItem from a JSON string
dashboard_acl_update_item_instance = DashboardACLUpdateItem.from_json(json)
# print the JSON string representation of the object
print DashboardACLUpdateItem.to_json()

# convert the object into a dict
dashboard_acl_update_item_dict = dashboard_acl_update_item_instance.to_dict()
# create an instance of DashboardACLUpdateItem from a dict
dashboard_acl_update_item_form_dict = dashboard_acl_update_item.from_dict(dashboard_acl_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


