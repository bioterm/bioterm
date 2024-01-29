# PauseAllAlertsCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paused** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.pause_all_alerts_command import PauseAllAlertsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PauseAllAlertsCommand from a JSON string
pause_all_alerts_command_instance = PauseAllAlertsCommand.from_json(json)
# print the JSON string representation of the object
print PauseAllAlertsCommand.to_json()

# convert the object into a dict
pause_all_alerts_command_dict = pause_all_alerts_command_instance.to_dict()
# create an instance of PauseAllAlertsCommand from a dict
pause_all_alerts_command_form_dict = pause_all_alerts_command.from_dict(pause_all_alerts_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


