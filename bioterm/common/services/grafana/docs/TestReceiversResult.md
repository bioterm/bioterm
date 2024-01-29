# TestReceiversResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | [**TestReceiversConfigAlertParams**](TestReceiversConfigAlertParams.md) |  | [optional] 
**notified_at** | **datetime** |  | [optional] 
**receivers** | [**List[TestReceiverResult]**](TestReceiverResult.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_receivers_result import TestReceiversResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestReceiversResult from a JSON string
test_receivers_result_instance = TestReceiversResult.from_json(json)
# print the JSON string representation of the object
print TestReceiversResult.to_json()

# convert the object into a dict
test_receivers_result_dict = test_receivers_result_instance.to_dict()
# create an instance of TestReceiversResult from a dict
test_receivers_result_form_dict = test_receivers_result.from_dict(test_receivers_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


