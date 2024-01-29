# PauseAlertCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | [optional] 
**paused** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.pause_alert_command import PauseAlertCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PauseAlertCommand from a JSON string
pause_alert_command_instance = PauseAlertCommand.from_json(json)
# print the JSON string representation of the object
print PauseAlertCommand.to_json()

# convert the object into a dict
pause_alert_command_dict = pause_alert_command_instance.to_dict()
# create an instance of PauseAlertCommand from a dict
pause_alert_command_form_dict = pause_alert_command.from_dict(pause_alert_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


