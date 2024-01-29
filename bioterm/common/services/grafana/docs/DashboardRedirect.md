# DashboardRedirect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_redirect import DashboardRedirect

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardRedirect from a JSON string
dashboard_redirect_instance = DashboardRedirect.from_json(json)
# print the JSON string representation of the object
print DashboardRedirect.to_json()

# convert the object into a dict
dashboard_redirect_dict = dashboard_redirect_instance.to_dict()
# create an instance of DashboardRedirect from a dict
dashboard_redirect_form_dict = dashboard_redirect.from_dict(dashboard_redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


