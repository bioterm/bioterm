# SlackConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[SlackAction]**](SlackAction.md) |  | [optional] 
**api_url** | [**URL**](URL.md) |  | [optional] 
**api_url_file** | **str** |  | [optional] 
**callback_id** | **str** |  | [optional] 
**channel** | **str** | Slack channel override, (like #other-channel or @username). | [optional] 
**color** | **str** |  | [optional] 
**fallback** | **str** |  | [optional] 
**fields** | [**List[SlackField]**](SlackField.md) |  | [optional] 
**footer** | **str** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**icon_emoji** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**link_names** | **bool** |  | [optional] 
**mrkdwn_in** | **List[str]** |  | [optional] 
**pretext** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**short_fields** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**thumb_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_link** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.slack_config import SlackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SlackConfig from a JSON string
slack_config_instance = SlackConfig.from_json(json)
# print the JSON string representation of the object
print SlackConfig.to_json()

# convert the object into a dict
slack_config_dict = slack_config_instance.to_dict()
# create an instance of SlackConfig from a dict
slack_config_form_dict = slack_config.from_dict(slack_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


