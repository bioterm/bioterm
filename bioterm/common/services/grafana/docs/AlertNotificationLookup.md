# AlertNotificationLookup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_notification_lookup import AlertNotificationLookup

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotificationLookup from a JSON string
alert_notification_lookup_instance = AlertNotificationLookup.from_json(json)
# print the JSON string representation of the object
print AlertNotificationLookup.to_json()

# convert the object into a dict
alert_notification_lookup_dict = alert_notification_lookup_instance.to_dict()
# create an instance of AlertNotificationLookup from a dict
alert_notification_lookup_form_dict = alert_notification_lookup.from_dict(alert_notification_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


