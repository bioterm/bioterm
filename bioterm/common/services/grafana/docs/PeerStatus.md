# PeerStatus

PeerStatus peer status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | 
**name** | **str** | name | 

## Example

```python
from grafanaApiClient.models.peer_status import PeerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PeerStatus from a JSON string
peer_status_instance = PeerStatus.from_json(json)
# print the JSON string representation of the object
print PeerStatus.to_json()

# convert the object into a dict
peer_status_dict = peer_status_instance.to_dict()
# create an instance of PeerStatus from a dict
peer_status_form_dict = peer_status.from_dict(peer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


