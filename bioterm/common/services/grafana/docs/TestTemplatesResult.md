# TestTemplatesResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the associated template definition for this result. | [optional] 
**text** | **str** | Interpolated value of the template. | [optional] 

## Example

```python
from grafanaApiClient.models.test_templates_result import TestTemplatesResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplatesResult from a JSON string
test_templates_result_instance = TestTemplatesResult.from_json(json)
# print the JSON string representation of the object
print TestTemplatesResult.to_json()

# convert the object into a dict
test_templates_result_dict = test_templates_result_instance.to_dict()
# create an instance of TestTemplatesResult from a dict
test_templates_result_form_dict = test_templates_result.from_dict(test_templates_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


