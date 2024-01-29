# AlertmanagerStatus

AlertmanagerStatus alertmanager status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ClusterStatus**](ClusterStatus.md) |  | 
**config** | [**AlertmanagerConfig**](AlertmanagerConfig.md) |  | 
**uptime** | **datetime** | uptime | 
**version_info** | [**VersionInfo**](VersionInfo.md) |  | 

## Example

```python
from grafanaApiClient.models.alertmanager_status import AlertmanagerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AlertmanagerStatus from a JSON string
alertmanager_status_instance = AlertmanagerStatus.from_json(json)
# print the JSON string representation of the object
print AlertmanagerStatus.to_json()

# convert the object into a dict
alertmanager_status_dict = alertmanager_status_instance.to_dict()
# create an instance of AlertmanagerStatus from a dict
alertmanager_status_form_dict = alertmanager_status.from_dict(alertmanager_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


