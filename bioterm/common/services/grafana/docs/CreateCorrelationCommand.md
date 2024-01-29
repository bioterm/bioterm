# CreateCorrelationCommand

CreateCorrelationCommand is the command for creating a correlation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**CorrelationConfig**](CorrelationConfig.md) |  | [optional] 
**description** | **str** | Optional description of the correlation | [optional] 
**label** | **str** | Optional label identifying the correlation | [optional] 
**provisioned** | **bool** | True if correlation was created with provisioning. This makes it read-only. | [optional] 
**target_uid** | **str** | Target data source UID to which the correlation is created. required if config.type &#x3D; query | [optional] 

## Example

```python
from grafanaApiClient.models.create_correlation_command import CreateCorrelationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCorrelationCommand from a JSON string
create_correlation_command_instance = CreateCorrelationCommand.from_json(json)
# print the JSON string representation of the object
print CreateCorrelationCommand.to_json()

# convert the object into a dict
create_correlation_command_dict = create_correlation_command_instance.to_dict()
# create an instance of CreateCorrelationCommand from a dict
create_correlation_command_form_dict = create_correlation_command.from_dict(create_correlation_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


