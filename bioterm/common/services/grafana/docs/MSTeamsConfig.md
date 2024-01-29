# MSTeamsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**webhook_url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.ms_teams_config import MSTeamsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MSTeamsConfig from a JSON string
ms_teams_config_instance = MSTeamsConfig.from_json(json)
# print the JSON string representation of the object
print MSTeamsConfig.to_json()

# convert the object into a dict
ms_teams_config_dict = ms_teams_config_instance.to_dict()
# create an instance of MSTeamsConfig from a dict
ms_teams_config_form_dict = ms_teams_config.from_dict(ms_teams_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


