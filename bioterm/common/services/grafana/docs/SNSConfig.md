# SNSConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**sigv4** | [**SigV4Config**](SigV4Config.md) |  | [optional] 
**subject** | **str** |  | [optional] 
**target_arn** | **str** |  | [optional] 
**topic_arn** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.sns_config import SNSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SNSConfig from a JSON string
sns_config_instance = SNSConfig.from_json(json)
# print the JSON string representation of the object
print SNSConfig.to_json()

# convert the object into a dict
sns_config_dict = sns_config_instance.to_dict()
# create an instance of SNSConfig from a dict
sns_config_form_dict = sns_config.from_dict(sns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


