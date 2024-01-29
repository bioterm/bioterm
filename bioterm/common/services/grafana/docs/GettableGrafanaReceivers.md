# GettableGrafanaReceivers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grafana_managed_receiver_configs** | [**List[GettableGrafanaReceiver]**](GettableGrafanaReceiver.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_grafana_receivers import GettableGrafanaReceivers

# TODO update the JSON string below
json = "{}"
# create an instance of GettableGrafanaReceivers from a JSON string
gettable_grafana_receivers_instance = GettableGrafanaReceivers.from_json(json)
# print the JSON string representation of the object
print GettableGrafanaReceivers.to_json()

# convert the object into a dict
gettable_grafana_receivers_dict = gettable_grafana_receivers_instance.to_dict()
# create an instance of GettableGrafanaReceivers from a dict
gettable_grafana_receivers_form_dict = gettable_grafana_receivers.from_dict(gettable_grafana_receivers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


