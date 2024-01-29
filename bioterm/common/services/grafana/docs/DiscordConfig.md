# DiscordConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**message** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**webhook_url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.discord_config import DiscordConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordConfig from a JSON string
discord_config_instance = DiscordConfig.from_json(json)
# print the JSON string representation of the object
print DiscordConfig.to_json()

# convert the object into a dict
discord_config_dict = discord_config_instance.to_dict()
# create an instance of DiscordConfig from a dict
discord_config_form_dict = discord_config.from_dict(discord_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


