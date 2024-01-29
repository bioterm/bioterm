# PublicDashboardListResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.public_dashboard_list_response import PublicDashboardListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicDashboardListResponse from a JSON string
public_dashboard_list_response_instance = PublicDashboardListResponse.from_json(json)
# print the JSON string representation of the object
print PublicDashboardListResponse.to_json()

# convert the object into a dict
public_dashboard_list_response_dict = public_dashboard_list_response_instance.to_dict()
# create an instance of PublicDashboardListResponse from a dict
public_dashboard_list_response_form_dict = public_dashboard_list_response.from_dict(public_dashboard_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


