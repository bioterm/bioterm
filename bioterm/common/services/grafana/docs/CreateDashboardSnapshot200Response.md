# CreateDashboardSnapshot200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_key** | **str** | Unique key used to delete the snapshot. It is different from the key so that only the creator can delete the snapshot. | [optional] 
**delete_url** | **str** |  | [optional] 
**id** | **int** | Snapshot id | [optional] 
**key** | **str** | Unique key | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_dashboard_snapshot200_response import CreateDashboardSnapshot200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardSnapshot200Response from a JSON string
create_dashboard_snapshot200_response_instance = CreateDashboardSnapshot200Response.from_json(json)
# print the JSON string representation of the object
print CreateDashboardSnapshot200Response.to_json()

# convert the object into a dict
create_dashboard_snapshot200_response_dict = create_dashboard_snapshot200_response_instance.to_dict()
# create an instance of CreateDashboardSnapshot200Response from a dict
create_dashboard_snapshot200_response_form_dict = create_dashboard_snapshot200_response.from_dict(create_dashboard_snapshot200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


