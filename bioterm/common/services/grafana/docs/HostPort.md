# HostPort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.host_port import HostPort

# TODO update the JSON string below
json = "{}"
# create an instance of HostPort from a JSON string
host_port_instance = HostPort.from_json(json)
# print the JSON string representation of the object
print HostPort.to_json()

# convert the object into a dict
host_port_dict = host_port_instance.to_dict()
# create an instance of HostPort from a dict
host_port_form_dict = host_port.from_dict(host_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


