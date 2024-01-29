# PostableNGalertConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanagers_choice** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_n_galert_config import PostableNGalertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostableNGalertConfig from a JSON string
postable_n_galert_config_instance = PostableNGalertConfig.from_json(json)
# print the JSON string representation of the object
print PostableNGalertConfig.to_json()

# convert the object into a dict
postable_n_galert_config_dict = postable_n_galert_config_instance.to_dict()
# create an instance of PostableNGalertConfig from a dict
postable_n_galert_config_form_dict = postable_n_galert_config.from_dict(postable_n_galert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


