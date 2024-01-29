# TestReceiversConfigBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | [**TestReceiversConfigAlertParams**](TestReceiversConfigAlertParams.md) |  | [optional] 
**receivers** | [**List[PostableApiReceiver]**](PostableApiReceiver.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_receivers_config_body_params import TestReceiversConfigBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of TestReceiversConfigBodyParams from a JSON string
test_receivers_config_body_params_instance = TestReceiversConfigBodyParams.from_json(json)
# print the JSON string representation of the object
print TestReceiversConfigBodyParams.to_json()

# convert the object into a dict
test_receivers_config_body_params_dict = test_receivers_config_body_params_instance.to_dict()
# create an instance of TestReceiversConfigBodyParams from a dict
test_receivers_config_body_params_form_dict = test_receivers_config_body_params.from_dict(test_receivers_config_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


