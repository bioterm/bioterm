# AlertNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**disable_resolve_message** | **bool** |  | [optional] 
**frequency** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**secure_fields** | **Dict[str, bool]** |  | [optional] 
**send_reminder** | **bool** |  | [optional] 
**settings** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_notification import AlertNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotification from a JSON string
alert_notification_instance = AlertNotification.from_json(json)
# print the JSON string representation of the object
print AlertNotification.to_json()

# convert the object into a dict
alert_notification_dict = alert_notification_instance.to_dict()
# create an instance of AlertNotification from a dict
alert_notification_form_dict = alert_notification.from_dict(alert_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


