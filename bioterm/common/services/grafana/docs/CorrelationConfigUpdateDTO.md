# CorrelationConfigUpdateDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field used to attach the correlation link | [optional] 
**target** | **object** | Target data query | [optional] 
**transformations** | [**List[Transformation]**](Transformation.md) | Source data transformations | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.correlation_config_update_dto import CorrelationConfigUpdateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationConfigUpdateDTO from a JSON string
correlation_config_update_dto_instance = CorrelationConfigUpdateDTO.from_json(json)
# print the JSON string representation of the object
print CorrelationConfigUpdateDTO.to_json()

# convert the object into a dict
correlation_config_update_dto_dict = correlation_config_update_dto_instance.to_dict()
# create an instance of CorrelationConfigUpdateDTO from a dict
correlation_config_update_dto_form_dict = correlation_config_update_dto.from_dict(correlation_config_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


