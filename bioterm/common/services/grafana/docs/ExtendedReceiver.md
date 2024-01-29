# ExtendedReceiver


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_configs** | [**EmailConfig**](EmailConfig.md) |  | [optional] 
**grafana_managed_receiver** | [**PostableGrafanaReceiver**](PostableGrafanaReceiver.md) |  | [optional] 
**opsgenie_configs** | [**OpsGenieConfig**](OpsGenieConfig.md) |  | [optional] 
**pagerduty_configs** | [**PagerdutyConfig**](PagerdutyConfig.md) |  | [optional] 
**pushover_configs** | [**PushoverConfig**](PushoverConfig.md) |  | [optional] 
**slack_configs** | [**SlackConfig**](SlackConfig.md) |  | [optional] 
**victorops_configs** | [**VictorOpsConfig**](VictorOpsConfig.md) |  | [optional] 
**webhook_configs** | [**WebhookConfig**](WebhookConfig.md) |  | [optional] 
**wechat_configs** | [**WechatConfig**](WechatConfig.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.extended_receiver import ExtendedReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedReceiver from a JSON string
extended_receiver_instance = ExtendedReceiver.from_json(json)
# print the JSON string representation of the object
print ExtendedReceiver.to_json()

# convert the object into a dict
extended_receiver_dict = extended_receiver_instance.to_dict()
# create an instance of ExtendedReceiver from a dict
extended_receiver_form_dict = extended_receiver.from_dict(extended_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


