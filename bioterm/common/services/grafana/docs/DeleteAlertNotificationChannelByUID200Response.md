# DeleteAlertNotificationChannelByUID200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID Identifier of the deleted notification channel. | 
**message** | **str** | Message Message of the deleted notificatiton channel. | 

## Example

```python
from grafanaApiClient.models.delete_alert_notification_channel_by_uid200_response import DeleteAlertNotificationChannelByUID200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAlertNotificationChannelByUID200Response from a JSON string
delete_alert_notification_channel_by_uid200_response_instance = DeleteAlertNotificationChannelByUID200Response.from_json(json)
# print the JSON string representation of the object
print DeleteAlertNotificationChannelByUID200Response.to_json()

# convert the object into a dict
delete_alert_notification_channel_by_uid200_response_dict = delete_alert_notification_channel_by_uid200_response_instance.to_dict()
# create an instance of DeleteAlertNotificationChannelByUID200Response from a dict
delete_alert_notification_channel_by_uid200_response_form_dict = delete_alert_notification_channel_by_uid200_response.from_dict(delete_alert_notification_channel_by_uid200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


