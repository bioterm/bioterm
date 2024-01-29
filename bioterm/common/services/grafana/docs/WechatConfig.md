# WechatConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | [optional] 
**api_secret** | **str** |  | [optional] 
**api_url** | [**URL**](URL.md) |  | [optional] 
**corp_id** | **str** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**to_party** | **str** |  | [optional] 
**to_tag** | **str** |  | [optional] 
**to_user** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.wechat_config import WechatConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WechatConfig from a JSON string
wechat_config_instance = WechatConfig.from_json(json)
# print the JSON string representation of the object
print WechatConfig.to_json()

# convert the object into a dict
wechat_config_dict = wechat_config_instance.to_dict()
# create an instance of WechatConfig from a dict
wechat_config_form_dict = wechat_config.from_dict(wechat_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


