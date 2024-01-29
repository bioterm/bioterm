# AlertTestCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**panel_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_test_command import AlertTestCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTestCommand from a JSON string
alert_test_command_instance = AlertTestCommand.from_json(json)
# print the JSON string representation of the object
print AlertTestCommand.to_json()

# convert the object into a dict
alert_test_command_dict = alert_test_command_instance.to_dict()
# create an instance of AlertTestCommand from a dict
alert_test_command_form_dict = alert_test_command.from_dict(alert_test_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


