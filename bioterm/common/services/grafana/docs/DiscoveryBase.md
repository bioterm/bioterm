# DiscoveryBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from grafanaApiClient.models.discovery_base import DiscoveryBase

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryBase from a JSON string
discovery_base_instance = DiscoveryBase.from_json(json)
# print the JSON string representation of the object
print DiscoveryBase.to_json()

# convert the object into a dict
discovery_base_dict = discovery_base_instance.to_dict()
# create an instance of DiscoveryBase from a dict
discovery_base_form_dict = discovery_base.from_dict(discovery_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


