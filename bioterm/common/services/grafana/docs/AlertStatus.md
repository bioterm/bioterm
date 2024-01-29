# AlertStatus

AlertStatus alert status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inhibited_by** | **List[str]** | inhibited by | 
**silenced_by** | **List[str]** | silenced by | 
**state** | **str** | state | 

## Example

```python
from grafanaApiClient.models.alert_status import AlertStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AlertStatus from a JSON string
alert_status_instance = AlertStatus.from_json(json)
# print the JSON string representation of the object
print AlertStatus.to_json()

# convert the object into a dict
alert_status_dict = alert_status_instance.to_dict()
# create an instance of AlertStatus from a dict
alert_status_form_dict = alert_status.from_dict(alert_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


