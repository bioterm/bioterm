# NotificationTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provenance** | **str** |  | [optional] 
**template** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.notification_template import NotificationTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplate from a JSON string
notification_template_instance = NotificationTemplate.from_json(json)
# print the JSON string representation of the object
print NotificationTemplate.to_json()

# convert the object into a dict
notification_template_dict = notification_template_instance.to_dict()
# create an instance of NotificationTemplate from a dict
notification_template_form_dict = notification_template.from_dict(notification_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


