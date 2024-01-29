# GlobalConfig

GlobalConfig defines configuration parameters that are valid globally unless overwritten.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**opsgenie_api_key** | **str** |  | [optional] 
**opsgenie_api_key_file** | **str** |  | [optional] 
**opsgenie_api_url** | [**URL**](URL.md) |  | [optional] 
**pagerduty_url** | [**URL**](URL.md) |  | [optional] 
**resolve_timeout** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**slack_api_url** | [**URL**](URL.md) |  | [optional] 
**slack_api_url_file** | **str** |  | [optional] 
**smtp_auth_identity** | **str** |  | [optional] 
**smtp_auth_password** | **str** |  | [optional] 
**smtp_auth_password_file** | **str** |  | [optional] 
**smtp_auth_secret** | **str** |  | [optional] 
**smtp_auth_username** | **str** |  | [optional] 
**smtp_from** | **str** |  | [optional] 
**smtp_hello** | **str** |  | [optional] 
**smtp_require_tls** | **bool** |  | [optional] 
**smtp_smarthost** | [**HostPort**](HostPort.md) |  | [optional] 
**telegram_api_url** | [**URL**](URL.md) |  | [optional] 
**victorops_api_key** | **str** |  | [optional] 
**victorops_api_key_file** | **str** |  | [optional] 
**victorops_api_url** | [**URL**](URL.md) |  | [optional] 
**webex_api_url** | [**URL**](URL.md) |  | [optional] 
**wechat_api_corp_id** | **str** |  | [optional] 
**wechat_api_secret** | **str** |  | [optional] 
**wechat_api_url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.global_config import GlobalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalConfig from a JSON string
global_config_instance = GlobalConfig.from_json(json)
# print the JSON string representation of the object
print GlobalConfig.to_json()

# convert the object into a dict
global_config_dict = global_config_instance.to_dict()
# create an instance of GlobalConfig from a dict
global_config_form_dict = global_config.from_dict(global_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


