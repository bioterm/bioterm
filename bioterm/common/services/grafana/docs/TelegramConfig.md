# TelegramConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | [**URL**](URL.md) |  | [optional] 
**chat** | **int** |  | [optional] 
**disable_notifications** | **bool** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**parse_mode** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**token_file** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.telegram_config import TelegramConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramConfig from a JSON string
telegram_config_instance = TelegramConfig.from_json(json)
# print the JSON string representation of the object
print TelegramConfig.to_json()

# convert the object into a dict
telegram_config_dict = telegram_config_instance.to_dict()
# create an instance of TelegramConfig from a dict
telegram_config_form_dict = telegram_config.from_dict(telegram_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


