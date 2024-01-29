# PublicDashboardListResponseWithPagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**public_dashboards** | [**List[PublicDashboardListResponse]**](PublicDashboardListResponse.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.public_dashboard_list_response_with_pagination import PublicDashboardListResponseWithPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PublicDashboardListResponseWithPagination from a JSON string
public_dashboard_list_response_with_pagination_instance = PublicDashboardListResponseWithPagination.from_json(json)
# print the JSON string representation of the object
print PublicDashboardListResponseWithPagination.to_json()

# convert the object into a dict
public_dashboard_list_response_with_pagination_dict = public_dashboard_list_response_with_pagination_instance.to_dict()
# create an instance of PublicDashboardListResponseWithPagination from a dict
public_dashboard_list_response_with_pagination_form_dict = public_dashboard_list_response_with_pagination.from_dict(public_dashboard_list_response_with_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


