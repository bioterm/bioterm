# DashboardFullWithMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**meta** | [**DashboardMeta**](DashboardMeta.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_full_with_meta import DashboardFullWithMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardFullWithMeta from a JSON string
dashboard_full_with_meta_instance = DashboardFullWithMeta.from_json(json)
# print the JSON string representation of the object
print DashboardFullWithMeta.to_json()

# convert the object into a dict
dashboard_full_with_meta_dict = dashboard_full_with_meta_instance.to_dict()
# create an instance of DashboardFullWithMeta from a dict
dashboard_full_with_meta_form_dict = dashboard_full_with_meta.from_dict(dashboard_full_with_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


