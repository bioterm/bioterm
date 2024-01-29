# NotificationPolicyExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**RouteExport**](RouteExport.md) |  | [optional] 
**org_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.notification_policy_export import NotificationPolicyExport

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPolicyExport from a JSON string
notification_policy_export_instance = NotificationPolicyExport.from_json(json)
# print the JSON string representation of the object
print NotificationPolicyExport.to_json()

# convert the object into a dict
notification_policy_export_dict = notification_policy_export_instance.to_dict()
# create an instance of NotificationPolicyExport from a dict
notification_policy_export_form_dict = notification_policy_export.from_dict(notification_policy_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


