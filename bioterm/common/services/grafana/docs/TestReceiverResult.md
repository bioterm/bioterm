# TestReceiverResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grafana_managed_receiver_configs** | [**List[TestReceiverConfigResult]**](TestReceiverConfigResult.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_receiver_result import TestReceiverResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestReceiverResult from a JSON string
test_receiver_result_instance = TestReceiverResult.from_json(json)
# print the JSON string representation of the object
print TestReceiverResult.to_json()

# convert the object into a dict
test_receiver_result_dict = test_receiver_result_instance.to_dict()
# create an instance of TestReceiverResult from a dict
test_receiver_result_form_dict = test_receiver_result.from_dict(test_receiver_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


