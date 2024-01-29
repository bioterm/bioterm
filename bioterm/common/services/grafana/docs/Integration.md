# Integration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_notify_attempt** | **datetime** | A timestamp indicating the last attempt to deliver a notification regardless of the outcome. Format: date-time | [optional] 
**last_notify_attempt_duration** | **str** | Duration of the last attempt to deliver a notification in humanized format (&#x60;1s&#x60; or &#x60;15ms&#x60;, etc). | [optional] 
**last_notify_attempt_error** | **str** | Error string for the last attempt to deliver a notification. Empty if the last attempt was successful. | [optional] 
**name** | **str** | name | 
**send_resolved** | **bool** | send resolved | 

## Example

```python
from grafanaApiClient.models.integration import Integration

# TODO update the JSON string below
json = "{}"
# create an instance of Integration from a JSON string
integration_instance = Integration.from_json(json)
# print the JSON string representation of the object
print Integration.to_json()

# convert the object into a dict
integration_dict = integration_instance.to_dict()
# create an instance of Integration from a dict
integration_form_dict = integration.from_dict(integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


