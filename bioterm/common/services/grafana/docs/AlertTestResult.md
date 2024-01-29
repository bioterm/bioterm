# AlertTestResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_evals** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**firing** | **bool** |  | [optional] 
**logs** | [**List[AlertTestResultLog]**](AlertTestResultLog.md) |  | [optional] 
**matches** | [**List[EvalMatch]**](EvalMatch.md) |  | [optional] 
**state** | **str** |  | [optional] 
**time_ms** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_test_result import AlertTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTestResult from a JSON string
alert_test_result_instance = AlertTestResult.from_json(json)
# print the JSON string representation of the object
print AlertTestResult.to_json()

# convert the object into a dict
alert_test_result_dict = alert_test_result_instance.to_dict()
# create an instance of AlertTestResult from a dict
alert_test_result_form_dict = alert_test_result.from_dict(alert_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


