# TestReceiverConfigResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_receiver_config_result import TestReceiverConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestReceiverConfigResult from a JSON string
test_receiver_config_result_instance = TestReceiverConfigResult.from_json(json)
# print the JSON string representation of the object
print TestReceiverConfigResult.to_json()

# convert the object into a dict
test_receiver_config_result_dict = test_receiver_config_result_instance.to_dict()
# create an instance of TestReceiverConfigResult from a dict
test_receiver_config_result_form_dict = test_receiver_config_result.from_dict(test_receiver_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


