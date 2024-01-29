# TestTemplatesResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[TestTemplatesErrorResult]**](TestTemplatesErrorResult.md) |  | [optional] 
**results** | [**List[TestTemplatesResult]**](TestTemplatesResult.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_templates_results import TestTemplatesResults

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplatesResults from a JSON string
test_templates_results_instance = TestTemplatesResults.from_json(json)
# print the JSON string representation of the object
print TestTemplatesResults.to_json()

# convert the object into a dict
test_templates_results_dict = test_templates_results_instance.to_dict()
# create an instance of TestTemplatesResults from a dict
test_templates_results_form_dict = test_templates_results.from_dict(test_templates_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


