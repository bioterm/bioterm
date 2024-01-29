# GettableGrafanaReceiver


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**provenance** | **str** |  | [optional] 
**secure_fields** | **Dict[str, bool]** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_grafana_receiver import GettableGrafanaReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of GettableGrafanaReceiver from a JSON string
gettable_grafana_receiver_instance = GettableGrafanaReceiver.from_json(json)
# print the JSON string representation of the object
print GettableGrafanaReceiver.to_json()

# convert the object into a dict
gettable_grafana_receiver_dict = gettable_grafana_receiver_instance.to_dict()
# create an instance of GettableGrafanaReceiver from a dict
gettable_grafana_receiver_form_dict = gettable_grafana_receiver.from_dict(gettable_grafana_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


