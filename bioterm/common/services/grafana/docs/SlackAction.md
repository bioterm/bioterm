# SlackAction

See https://api.slack.com/docs/message-attachments#action_fields and https://api.slack.com/docs/message-buttons for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm** | [**SlackConfirmationField**](SlackConfirmationField.md) |  | [optional] 
**name** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.slack_action import SlackAction

# TODO update the JSON string below
json = "{}"
# create an instance of SlackAction from a JSON string
slack_action_instance = SlackAction.from_json(json)
# print the JSON string representation of the object
print SlackAction.to_json()

# convert the object into a dict
slack_action_dict = slack_action_instance.to_dict()
# create an instance of SlackAction from a dict
slack_action_form_dict = slack_action.from_dict(slack_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


