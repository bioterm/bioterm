# NotificationTestCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**frequency** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**secure_settings** | **Dict[str, str]** |  | [optional] 
**send_reminder** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.notification_test_command import NotificationTestCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestCommand from a JSON string
notification_test_command_instance = NotificationTestCommand.from_json(json)
# print the JSON string representation of the object
print NotificationTestCommand.to_json()

# convert the object into a dict
notification_test_command_dict = notification_test_command_instance.to_dict()
# create an instance of NotificationTestCommand from a dict
notification_test_command_form_dict = notification_test_command.from_dict(notification_test_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


