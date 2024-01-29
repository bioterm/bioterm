# Threshold

Threshold a single step on the threshold list

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**value** | **float** | ConfFloat64 is a float64. It Marshals float64 values of NaN of Inf to null. | [optional] 

## Example

```python
from grafanaApiClient.models.threshold import Threshold

# TODO update the JSON string below
json = "{}"
# create an instance of Threshold from a JSON string
threshold_instance = Threshold.from_json(json)
# print the JSON string representation of the object
print Threshold.to_json()

# convert the object into a dict
threshold_dict = threshold_instance.to_dict()
# create an instance of Threshold from a dict
threshold_form_dict = threshold.from_dict(threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


