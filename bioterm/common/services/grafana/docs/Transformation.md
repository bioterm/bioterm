# Transformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 
**field** | **str** |  | [optional] 
**map_value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.transformation import Transformation

# TODO update the JSON string below
json = "{}"
# create an instance of Transformation from a JSON string
transformation_instance = Transformation.from_json(json)
# print the JSON string representation of the object
print Transformation.to_json()

# convert the object into a dict
transformation_dict = transformation_instance.to_dict()
# create an instance of Transformation from a dict
transformation_form_dict = transformation.from_dict(transformation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


