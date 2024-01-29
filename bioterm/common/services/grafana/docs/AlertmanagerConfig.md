# AlertmanagerConfig

AlertmanagerConfig alertmanager config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | original | 

## Example

```python
from grafanaApiClient.models.alertmanager_config import AlertmanagerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AlertmanagerConfig from a JSON string
alertmanager_config_instance = AlertmanagerConfig.from_json(json)
# print the JSON string representation of the object
print AlertmanagerConfig.to_json()

# convert the object into a dict
alertmanager_config_dict = alertmanager_config_instance.to_dict()
# create an instance of AlertmanagerConfig from a dict
alertmanager_config_form_dict = alertmanager_config.from_dict(alertmanager_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


