# CreateAlertNotificationCommand


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
from grafanaApiClient.models.create_alert_notification_command import CreateAlertNotificationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertNotificationCommand from a JSON string
create_alert_notification_command_instance = CreateAlertNotificationCommand.from_json(json)
# print the JSON string representation of the object
print CreateAlertNotificationCommand.to_json()

# convert the object into a dict
create_alert_notification_command_dict = create_alert_notification_command_instance.to_dict()
# create an instance of CreateAlertNotificationCommand from a dict
create_alert_notification_command_form_dict = create_alert_notification_command.from_dict(create_alert_notification_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


