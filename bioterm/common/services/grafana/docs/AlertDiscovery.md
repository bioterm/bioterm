# AlertDiscovery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[Alert]**](Alert.md) |  | 

## Example

```python
from grafanaApiClient.models.alert_discovery import AlertDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of AlertDiscovery from a JSON string
alert_discovery_instance = AlertDiscovery.from_json(json)
# print the JSON string representation of the object
print AlertDiscovery.to_json()

# convert the object into a dict
alert_discovery_dict = alert_discovery_instance.to_dict()
# create an instance of AlertDiscovery from a dict
alert_discovery_form_dict = alert_discovery.from_dict(alert_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


