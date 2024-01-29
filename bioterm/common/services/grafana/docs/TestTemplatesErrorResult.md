# TestTemplatesErrorResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind of template error that occurred. | [optional] 
**message** | **str** | Error message. | [optional] 
**name** | **str** | Name of the associated template for this error. Will be empty if the Kind is \&quot;invalid_template\&quot;. | [optional] 

## Example

```python
from grafanaApiClient.models.test_templates_error_result import TestTemplatesErrorResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplatesErrorResult from a JSON string
test_templates_error_result_instance = TestTemplatesErrorResult.from_json(json)
# print the JSON string representation of the object
print TestTemplatesErrorResult.to_json()

# convert the object into a dict
test_templates_error_result_dict = test_templates_error_result_instance.to_dict()
# create an instance of TestTemplatesErrorResult from a dict
test_templates_error_result_form_dict = test_templates_error_result.from_dict(test_templates_error_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


