# NotifierConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_resolved** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.notifier_config import NotifierConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NotifierConfig from a JSON string
notifier_config_instance = NotifierConfig.from_json(json)
# print the JSON string representation of the object
print NotifierConfig.to_json()

# convert the object into a dict
notifier_config_dict = notifier_config_instance.to_dict()
# create an instance of NotifierConfig from a dict
notifier_config_form_dict = notifier_config.from_dict(notifier_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


