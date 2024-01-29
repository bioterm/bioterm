# AlertManagersResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_alert_managers** | [**List[AlertManager]**](AlertManager.md) |  | [optional] 
**dropped_alert_managers** | [**List[AlertManager]**](AlertManager.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_managers_result import AlertManagersResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertManagersResult from a JSON string
alert_managers_result_instance = AlertManagersResult.from_json(json)
# print the JSON string representation of the object
print AlertManagersResult.to_json()

# convert the object into a dict
alert_managers_result_dict = alert_managers_result_instance.to_dict()
# create an instance of AlertManagersResult from a dict
alert_managers_result_form_dict = alert_managers_result.from_dict(alert_managers_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


