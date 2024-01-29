# UpdateCorrelationCommand

UpdateCorrelationCommand is the command for updating a correlation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**CorrelationConfigUpdateDTO**](CorrelationConfigUpdateDTO.md) |  | [optional] 
**description** | **str** | Optional description of the correlation | [optional] 
**label** | **str** | Optional label identifying the correlation | [optional] 

## Example

```python
from grafanaApiClient.models.update_correlation_command import UpdateCorrelationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCorrelationCommand from a JSON string
update_correlation_command_instance = UpdateCorrelationCommand.from_json(json)
# print the JSON string representation of the object
print UpdateCorrelationCommand.to_json()

# convert the object into a dict
update_correlation_command_dict = update_correlation_command_instance.to_dict()
# create an instance of UpdateCorrelationCommand from a dict
update_correlation_command_form_dict = update_correlation_command.from_dict(update_correlation_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


