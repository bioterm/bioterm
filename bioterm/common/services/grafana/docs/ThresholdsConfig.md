# ThresholdsConfig

ThresholdsConfig setup thresholds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | ThresholdsMode absolute or percentage | [optional] 
**steps** | [**List[Threshold]**](Threshold.md) | Must be sorted by &#39;value&#39;, first value is always -Infinity | [optional] 

## Example

```python
from grafanaApiClient.models.thresholds_config import ThresholdsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdsConfig from a JSON string
thresholds_config_instance = ThresholdsConfig.from_json(json)
# print the JSON string representation of the object
print ThresholdsConfig.to_json()

# convert the object into a dict
thresholds_config_dict = thresholds_config_instance.to_dict()
# create an instance of ThresholdsConfig from a dict
thresholds_config_form_dict = thresholds_config.from_dict(thresholds_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


