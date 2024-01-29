# Notice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inspect** | **int** |  | [optional] 
**link** | **str** | Link is an optional link for display in the user interface and can be an absolute URL or a path relative to Grafana&#39;s root url. | [optional] 
**severity** | **int** |  | [optional] 
**text** | **str** | Text is freeform descriptive text for the notice. | [optional] 

## Example

```python
from grafanaApiClient.models.notice import Notice

# TODO update the JSON string below
json = "{}"
# create an instance of Notice from a JSON string
notice_instance = Notice.from_json(json)
# print the JSON string representation of the object
print Notice.to_json()

# convert the object into a dict
notice_dict = notice_instance.to_dict()
# create an instance of Notice from a dict
notice_form_dict = notice.from_dict(notice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


