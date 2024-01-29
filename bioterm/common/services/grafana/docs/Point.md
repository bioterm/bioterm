# Point

If H is not nil, then this is a histogram point and only (T, H) is valid. If H is nil, then only (T, V) is valid.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h** | [**FloatHistogram**](FloatHistogram.md) |  | [optional] 
**t** | **int** |  | [optional] 
**v** | **float** |  | [optional] 

## Example

```python
from grafanaApiClient.models.point import Point

# TODO update the JSON string below
json = "{}"
# create an instance of Point from a JSON string
point_instance = Point.from_json(json)
# print the JSON string representation of the object
print Point.to_json()

# convert the object into a dict
point_dict = point_instance.to_dict()
# create an instance of Point from a dict
point_form_dict = point.from_dict(point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


