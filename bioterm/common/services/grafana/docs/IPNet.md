# IPNet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**mask** | **List[int]** | See type IPNet and func ParseCIDR for details. | [optional] 

## Example

```python
from grafanaApiClient.models.ip_net import IPNet

# TODO update the JSON string below
json = "{}"
# create an instance of IPNet from a JSON string
ip_net_instance = IPNet.from_json(json)
# print the JSON string representation of the object
print IPNet.to_json()

# convert the object into a dict
ip_net_dict = ip_net_instance.to_dict()
# create an instance of IPNet from a dict
ip_net_form_dict = ip_net.from_dict(ip_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


