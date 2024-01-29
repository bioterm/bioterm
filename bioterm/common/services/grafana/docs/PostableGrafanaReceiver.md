# PostableGrafanaReceiver


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resolve_message** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**secure_settings** | **Dict[str, str]** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_grafana_receiver import PostableGrafanaReceiver

# TODO update the JSON string below
json = "{}"
# create an instance of PostableGrafanaReceiver from a JSON string
postable_grafana_receiver_instance = PostableGrafanaReceiver.from_json(json)
# print the JSON string representation of the object
print PostableGrafanaReceiver.to_json()

# convert the object into a dict
postable_grafana_receiver_dict = postable_grafana_receiver_instance.to_dict()
# create an instance of PostableGrafanaReceiver from a dict
postable_grafana_receiver_form_dict = postable_grafana_receiver.from_dict(postable_grafana_receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


