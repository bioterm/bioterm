# ImportDashboardInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.import_dashboard_input import ImportDashboardInput

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDashboardInput from a JSON string
import_dashboard_input_instance = ImportDashboardInput.from_json(json)
# print the JSON string representation of the object
print ImportDashboardInput.to_json()

# convert the object into a dict
import_dashboard_input_dict = import_dashboard_input_instance.to_dict()
# create an instance of ImportDashboardInput from a dict
import_dashboard_input_form_dict = import_dashboard_input.from_dict(import_dashboard_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


