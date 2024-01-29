# GettableUserConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanager_config** | [**GettableApiAlertingConfig**](GettableApiAlertingConfig.md) |  | [optional] 
**template_file_provenances** | **Dict[str, str]** |  | [optional] 
**template_files** | **Dict[str, str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_user_config import GettableUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GettableUserConfig from a JSON string
gettable_user_config_instance = GettableUserConfig.from_json(json)
# print the JSON string representation of the object
print GettableUserConfig.to_json()

# convert the object into a dict
gettable_user_config_dict = gettable_user_config_instance.to_dict()
# create an instance of GettableUserConfig from a dict
gettable_user_config_form_dict = gettable_user_config.from_dict(gettable_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


