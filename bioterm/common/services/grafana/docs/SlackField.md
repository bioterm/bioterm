# SlackField

Each field must contain a title, value, and optionally, a boolean value to indicate if the field is short enough to be displayed next to other fields designated as short. See https://api.slack.com/docs/message-attachments#fields for more information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.slack_field import SlackField

# TODO update the JSON string below
json = "{}"
# create an instance of SlackField from a JSON string
slack_field_instance = SlackField.from_json(json)
# print the JSON string representation of the object
print SlackField.to_json()

# convert the object into a dict
slack_field_dict = slack_field_instance.to_dict()
# create an instance of SlackField from a dict
slack_field_form_dict = slack_field.from_dict(slack_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


