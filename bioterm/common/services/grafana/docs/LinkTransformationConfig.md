# LinkTransformationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 
**field** | **str** |  | [optional] 
**map_value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.link_transformation_config import LinkTransformationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LinkTransformationConfig from a JSON string
link_transformation_config_instance = LinkTransformationConfig.from_json(json)
# print the JSON string representation of the object
print LinkTransformationConfig.to_json()

# convert the object into a dict
link_transformation_config_dict = link_transformation_config_instance.to_dict()
# create an instance of LinkTransformationConfig from a dict
link_transformation_config_form_dict = link_transformation_config.from_dict(link_transformation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


