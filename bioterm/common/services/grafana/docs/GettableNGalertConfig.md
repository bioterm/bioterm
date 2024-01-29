# GettableNGalertConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanagers_choice** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_n_galert_config import GettableNGalertConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GettableNGalertConfig from a JSON string
gettable_n_galert_config_instance = GettableNGalertConfig.from_json(json)
# print the JSON string representation of the object
print GettableNGalertConfig.to_json()

# convert the object into a dict
gettable_n_galert_config_dict = gettable_n_galert_config_instance.to_dict()
# create an instance of GettableNGalertConfig from a dict
gettable_n_galert_config_form_dict = gettable_n_galert_config.from_dict(gettable_n_galert_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


