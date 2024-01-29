# GettableHistoricUserConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanager_config** | [**GettableApiAlertingConfig**](GettableApiAlertingConfig.md) |  | [optional] 
**id** | **int** |  | [optional] 
**last_applied** | **datetime** |  | [optional] 
**template_file_provenances** | **Dict[str, str]** |  | [optional] 
**template_files** | **Dict[str, str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_historic_user_config import GettableHistoricUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GettableHistoricUserConfig from a JSON string
gettable_historic_user_config_instance = GettableHistoricUserConfig.from_json(json)
# print the JSON string representation of the object
print GettableHistoricUserConfig.to_json()

# convert the object into a dict
gettable_historic_user_config_dict = gettable_historic_user_config_instance.to_dict()
# create an instance of GettableHistoricUserConfig from a dict
gettable_historic_user_config_form_dict = gettable_historic_user_config.from_dict(gettable_historic_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


