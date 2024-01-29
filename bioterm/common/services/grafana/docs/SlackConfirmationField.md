# SlackConfirmationField

SlackConfirmationField protect users from destructive actions or particularly distinguished decisions by asking them to confirm their button click one more time. See https://api.slack.com/docs/interactive-message-field-guide#confirmation_fields for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dismiss_text** | **str** |  | [optional] 
**ok_text** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.slack_confirmation_field import SlackConfirmationField

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfirmationField from a JSON string
slack_confirmation_field_instance = SlackConfirmationField.from_json(json)
# print the JSON string representation of the object
print SlackConfirmationField.to_json()

# convert the object into a dict
slack_confirmation_field_dict = slack_confirmation_field_instance.to_dict()
# create an instance of SlackConfirmationField from a dict
slack_confirmation_field_form_dict = slack_confirmation_field.from_dict(slack_confirmation_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


