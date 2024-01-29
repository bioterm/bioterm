# EvalAlertConditionCommand

EvalAlertConditionCommand is the command for evaluating a condition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** |  | [optional] 
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | [optional] 
**now** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.eval_alert_condition_command import EvalAlertConditionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EvalAlertConditionCommand from a JSON string
eval_alert_condition_command_instance = EvalAlertConditionCommand.from_json(json)
# print the JSON string representation of the object
print EvalAlertConditionCommand.to_json()

# convert the object into a dict
eval_alert_condition_command_dict = eval_alert_condition_command_instance.to_dict()
# create an instance of EvalAlertConditionCommand from a dict
eval_alert_condition_command_form_dict = eval_alert_condition_command.from_dict(eval_alert_condition_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


