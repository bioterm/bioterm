# PaginatedNotificationTransportList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[NotificationTransport]**](NotificationTransport.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_notification_transport_list import PaginatedNotificationTransportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNotificationTransportList from a JSON string
paginated_notification_transport_list_instance = PaginatedNotificationTransportList.from_json(json)
# print the JSON string representation of the object
print PaginatedNotificationTransportList.to_json()

# convert the object into a dict
paginated_notification_transport_list_dict = paginated_notification_transport_list_instance.to_dict()
# create an instance of PaginatedNotificationTransportList from a dict
paginated_notification_transport_list_form_dict = paginated_notification_transport_list.from_dict(paginated_notification_transport_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


