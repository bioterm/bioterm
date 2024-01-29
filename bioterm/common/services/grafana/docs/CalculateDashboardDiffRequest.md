# CalculateDashboardDiffRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**CalculateDiffTarget**](CalculateDiffTarget.md) |  | [optional] 
**diff_type** | **str** | The type of diff to return Description: &#x60;basic&#x60; &#x60;json&#x60; | [optional] 
**new** | [**CalculateDiffTarget**](CalculateDiffTarget.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.calculate_dashboard_diff_request import CalculateDashboardDiffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateDashboardDiffRequest from a JSON string
calculate_dashboard_diff_request_instance = CalculateDashboardDiffRequest.from_json(json)
# print the JSON string representation of the object
print CalculateDashboardDiffRequest.to_json()

# convert the object into a dict
calculate_dashboard_diff_request_dict = calculate_dashboard_diff_request_instance.to_dict()
# create an instance of CalculateDashboardDiffRequest from a dict
calculate_dashboard_diff_request_form_dict = calculate_dashboard_diff_request.from_dict(calculate_dashboard_diff_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


