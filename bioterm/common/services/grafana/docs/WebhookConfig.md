# WebhookConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**max_alerts** | **int** | MaxAlerts is the maximum number of alerts to be sent per webhook message. Alerts exceeding this threshold will be truncated. Setting this to 0 allows an unlimited number of alerts. | [optional] 
**send_resolved** | **bool** |  | [optional] 
**url** | [**URL**](URL.md) |  | [optional] 
**url_file** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.webhook_config import WebhookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookConfig from a JSON string
webhook_config_instance = WebhookConfig.from_json(json)
# print the JSON string representation of the object
print WebhookConfig.to_json()

# convert the object into a dict
webhook_config_dict = webhook_config_instance.to_dict()
# create an instance of WebhookConfig from a dict
webhook_config_form_dict = webhook_config.from_dict(webhook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


