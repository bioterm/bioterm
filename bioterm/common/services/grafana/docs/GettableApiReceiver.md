# GettableApiReceiver


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_configs** | [**List[DiscordConfig]**](DiscordConfig.md) |  | [optional] 
**email_configs** | [**List[EmailConfig]**](EmailConfig.md) |  | [optional] 
**grafana_managed_receiver_configs** | [**List[GettableGrafanaReceiver]**](GettableGrafanaReceiver.md) |  | [optional] 
**msteams_configs** | [**List[MSTeamsConfig]**](MSTeamsConfig.md) |  | [optional] 
**name** | **str** | A unique identifier for this receiver. | [optional] 
**opsgenie_configs** | [**List[OpsGenieConfig]**](OpsGenieConfig.md) |  | [optional] 
**pagerduty_configs** | [**List[PagerdutyConfig]**](PagerdutyConfig.md) |  | [optional] 
**pushover_configs** | [**List[PushoverConfig]**](PushoverConfig.md) |  | [optional] 
**slack_configs** | [**List[SlackConfig]**](SlackConfig.md) |  | [optional] 
**sns_configs** | [**List[SNSConfig]**](SNSConfig.md) |  | [optional] 
**telegram_configs** | [**List[TelegramConfig]**](TelegramConfig.md) |  | [optional] 
**victorops_configs** | [**List[VictorOpsConfig]**](VictorOpsConfig.md) |  | [optional] 
**webex_configs** | [**List[WebexConfig]**](WebexConfig.md) |  | [optional] 
**webhook_configs** | [**List[WebhookConfig]**](WebhookConfig.md) |  | [optional] 
**wechat_configs** | [**List[WechatConfig]**](WechatConfig.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_api_receiver import GettableApiReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of GettableApiReceiver from a JSON string
gettable_api_receiver_instance = GettableApiReceiver.from_json(json)
# print the JSON string representation of the object
print GettableApiReceiver.to_json()

# convert the object into a dict
gettable_api_receiver_dict = gettable_api_receiver_instance.to_dict()
# create an instance of GettableApiReceiver from a dict
gettable_api_receiver_form_dict = gettable_api_receiver.from_dict(gettable_api_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


