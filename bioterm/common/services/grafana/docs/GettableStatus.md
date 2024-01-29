# GettableStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ClusterStatus**](ClusterStatus.md) |  | 
**config** | [**PostableApiAlertingConfig**](PostableApiAlertingConfig.md) |  | 
**uptime** | **datetime** | uptime | 
**version_info** | [**VersionInfo**](VersionInfo.md) |  | 

## Example

```python
from grafanaApiClient.models.gettable_status import GettableStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GettableStatus from a JSON string
gettable_status_instance = GettableStatus.from_json(json)
# print the JSON string representation of the object
print GettableStatus.to_json()

# convert the object into a dict
gettable_status_dict = gettable_status_instance.to_dict()
# create an instance of GettableStatus from a dict
gettable_status_form_dict = gettable_status.from_dict(gettable_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


