# UpdateAlertNotificationWithUidCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**frequency** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**secure_settings** | **Dict[str, str]** |  | [optional] 
**send_reminder** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_alert_notification_with_uid_command import UpdateAlertNotificationWithUidCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertNotificationWithUidCommand from a JSON string
update_alert_notification_with_uid_command_instance = UpdateAlertNotificationWithUidCommand.from_json(json)
# print the JSON string representation of the object
print UpdateAlertNotificationWithUidCommand.to_json()

# convert the object into a dict
update_alert_notification_with_uid_command_dict = update_alert_notification_with_uid_command_instance.to_dict()
# create an instance of UpdateAlertNotificationWithUidCommand from a dict
update_alert_notification_with_uid_command_form_dict = update_alert_notification_with_uid_command.from_dict(update_alert_notification_with_uid_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


