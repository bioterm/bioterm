# PostableUserConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanager_config** | [**PostableApiAlertingConfig**](PostableApiAlertingConfig.md) |  | [optional] 
**template_files** | **Dict[str, str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_user_config import PostableUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostableUserConfig from a JSON string
postable_user_config_instance = PostableUserConfig.from_json(json)
# print the JSON string representation of the object
print PostableUserConfig.to_json()

# convert the object into a dict
postable_user_config_dict = postable_user_config_instance.to_dict()
# create an instance of PostableUserConfig from a dict
postable_user_config_form_dict = postable_user_config.from_dict(postable_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


