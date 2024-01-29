# NotificationTemplateContent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.notification_template_content import NotificationTemplateContent

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateContent from a JSON string
notification_template_content_instance = NotificationTemplateContent.from_json(json)
# print the JSON string representation of the object
print NotificationTemplateContent.to_json()

# convert the object into a dict
notification_template_content_dict = notification_template_content_instance.to_dict()
# create an instance of NotificationTemplateContent from a dict
notification_template_content_form_dict = notification_template_content.from_dict(notification_template_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


