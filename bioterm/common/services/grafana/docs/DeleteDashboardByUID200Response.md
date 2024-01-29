# DeleteDashboardByUID200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID Identifier of the deleted dashboard. | 
**message** | **str** | Message Message of the deleted dashboard. | 
**title** | **str** | Title Title of the deleted dashboard. | 

## Example

```python
from grafanaApiClient.models.delete_dashboard_by_uid200_response import DeleteDashboardByUID200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDashboardByUID200Response from a JSON string
delete_dashboard_by_uid200_response_instance = DeleteDashboardByUID200Response.from_json(json)
# print the JSON string representation of the object
print DeleteDashboardByUID200Response.to_json()

# convert the object into a dict
delete_dashboard_by_uid200_response_dict = delete_dashboard_by_uid200_response_instance.to_dict()
# create an instance of DeleteDashboardByUID200Response from a dict
delete_dashboard_by_uid200_response_form_dict = delete_dashboard_by_uid200_response.from_dict(delete_dashboard_by_uid200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


