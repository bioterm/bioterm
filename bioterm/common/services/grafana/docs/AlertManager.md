# AlertManager


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_manager import AlertManager

# TODO update the JSON string below
json = "{}"
# create an instance of AlertManager from a JSON string
alert_manager_instance = AlertManager.from_json(json)
# print the JSON string representation of the object
print AlertManager.to_json()

# convert the object into a dict
alert_manager_dict = alert_manager_instance.to_dict()
# create an instance of AlertManager from a dict
alert_manager_form_dict = alert_manager.from_dict(alert_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


