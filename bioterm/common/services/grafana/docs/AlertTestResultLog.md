# AlertTestResultLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_test_result_log import AlertTestResultLog

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTestResultLog from a JSON string
alert_test_result_log_instance = AlertTestResultLog.from_json(json)
# print the JSON string representation of the object
print AlertTestResultLog.to_json()

# convert the object into a dict
alert_test_result_log_dict = alert_test_result_log_instance.to_dict()
# create an instance of AlertTestResultLog from a dict
alert_test_result_log_form_dict = alert_test_result_log.from_dict(alert_test_result_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


