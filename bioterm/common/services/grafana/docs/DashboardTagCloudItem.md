# DashboardTagCloudItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**term** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_tag_cloud_item import DashboardTagCloudItem

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardTagCloudItem from a JSON string
dashboard_tag_cloud_item_instance = DashboardTagCloudItem.from_json(json)
# print the JSON string representation of the object
print DashboardTagCloudItem.to_json()

# convert the object into a dict
dashboard_tag_cloud_item_dict = dashboard_tag_cloud_item_instance.to_dict()
# create an instance of DashboardTagCloudItem from a dict
dashboard_tag_cloud_item_form_dict = dashboard_tag_cloud_item.from_dict(dashboard_tag_cloud_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


