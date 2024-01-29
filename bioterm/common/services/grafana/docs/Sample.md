# Sample


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h** | [**FloatHistogram**](FloatHistogram.md) |  | [optional] 
**metric** | [**List[Label]**](Label.md) | Labels is a sorted set of labels. Order has to be guaranteed upon instantiation. | [optional] 
**t** | **int** |  | [optional] 
**v** | **float** |  | [optional] 

## Example

```python
from grafanaApiClient.models.sample import Sample

# TODO update the JSON string below
json = "{}"
# create an instance of Sample from a JSON string
sample_instance = Sample.from_json(json)
# print the JSON string representation of the object
print Sample.to_json()

# convert the object into a dict
sample_dict = sample_instance.to_dict()
# create an instance of Sample from a dict
sample_form_dict = sample.from_dict(sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


