# GetHomeDashboardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**meta** | [**DashboardMeta**](DashboardMeta.md) |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.get_home_dashboard_response import GetHomeDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHomeDashboardResponse from a JSON string
get_home_dashboard_response_instance = GetHomeDashboardResponse.from_json(json)
# print the JSON string representation of the object
print GetHomeDashboardResponse.to_json()

# convert the object into a dict
get_home_dashboard_response_dict = get_home_dashboard_response_instance.to_dict()
# create an instance of GetHomeDashboardResponse from a dict
get_home_dashboard_response_form_dict = get_home_dashboard_response.from_dict(get_home_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


