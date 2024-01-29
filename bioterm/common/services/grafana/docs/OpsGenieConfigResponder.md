# OpsGenieConfigResponder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | One of those 3 should be filled. | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | team, user, escalation, schedule etc. | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.ops_genie_config_responder import OpsGenieConfigResponder

# TODO update the JSON string below
json = "{}"
# create an instance of OpsGenieConfigResponder from a JSON string
ops_genie_config_responder_instance = OpsGenieConfigResponder.from_json(json)
# print the JSON string representation of the object
print OpsGenieConfigResponder.to_json()

# convert the object into a dict
ops_genie_config_responder_dict = ops_genie_config_responder_instance.to_dict()
# create an instance of OpsGenieConfigResponder from a dict
ops_genie_config_responder_form_dict = ops_genie_config_responder.from_dict(ops_genie_config_responder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


