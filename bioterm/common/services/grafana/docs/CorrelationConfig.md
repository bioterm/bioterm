# CorrelationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field used to attach the correlation link | 
**target** | **object** | Target data query | 
**transformations** | [**List[Transformation]**](Transformation.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from grafanaApiClient.models.correlation_config import CorrelationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationConfig from a JSON string
correlation_config_instance = CorrelationConfig.from_json(json)
# print the JSON string representation of the object
print CorrelationConfig.to_json()

# convert the object into a dict
correlation_config_dict = correlation_config_instance.to_dict()
# create an instance of CorrelationConfig from a dict
correlation_config_form_dict = correlation_config.from_dict(correlation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


