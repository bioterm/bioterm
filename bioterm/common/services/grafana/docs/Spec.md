# Spec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie_preferences** | [**CookiePreferences**](CookiePreferences.md) |  | [optional] 
**home_dashboard_uid** | **str** | UID for the home dashboard | [optional] 
**language** | **str** | Selected language (beta) | [optional] 
**query_history** | [**QueryHistoryPreference**](QueryHistoryPreference.md) |  | [optional] 
**theme** | **str** | Theme light, dark, empty is default | [optional] 
**timezone** | **str** | The timezone selection TODO: this should use the timezone defined in common | [optional] 
**week_start** | **str** | WeekStart day of the week (sunday, monday, etc) | [optional] 

## Example

```python
from grafanaApiClient.models.spec import Spec

# TODO update the JSON string below
json = "{}"
# create an instance of Spec from a JSON string
spec_instance = Spec.from_json(json)
# print the JSON string representation of the object
print Spec.to_json()

# convert the object into a dict
spec_dict = spec_instance.to_dict()
# create an instance of Spec from a dict
spec_form_dict = spec.from_dict(spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


