# PostDashboard200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_uid** | **str** | FolderUID The unique identifier (uid) of the folder the dashboard belongs to. | [optional] 
**id** | **int** | ID The unique identifier (id) of the created/updated dashboard. | 
**status** | **str** | Status status of the response. | 
**title** | **str** | Slug The slug of the dashboard. | 
**uid** | **str** | UID The unique identifier (uid) of the created/updated dashboard. | 
**url** | **str** | URL The relative URL for accessing the created/updated dashboard. | 
**version** | **int** | Version The version of the dashboard. | 

## Example

```python
from grafanaApiClient.models.post_dashboard200_response import PostDashboard200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostDashboard200Response from a JSON string
post_dashboard200_response_instance = PostDashboard200Response.from_json(json)
# print the JSON string representation of the object
print PostDashboard200Response.to_json()

# convert the object into a dict
post_dashboard200_response_dict = post_dashboard200_response_instance.to_dict()
# create an instance of PostDashboard200Response from a dict
post_dashboard200_response_form_dict = post_dashboard200_response.from_dict(post_dashboard200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


