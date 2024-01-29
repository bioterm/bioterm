# TestTemplatesConfigBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[PostableAlert]**](PostableAlert.md) | Alerts to use as data when testing the template. | [optional] 
**name** | **str** | Name of the template file. | [optional] 
**template** | **str** | Template string to test. | [optional] 

## Example

```python
from grafanaApiClient.models.test_templates_config_body_params import TestTemplatesConfigBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of TestTemplatesConfigBodyParams from a JSON string
test_templates_config_body_params_instance = TestTemplatesConfigBodyParams.from_json(json)
# print the JSON string representation of the object
print TestTemplatesConfigBodyParams.to_json()

# convert the object into a dict
test_templates_config_body_params_dict = test_templates_config_body_params_instance.to_dict()
# create an instance of TestTemplatesConfigBodyParams from a dict
test_templates_config_body_params_form_dict = test_templates_config_body_params.from_dict(test_templates_config_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


