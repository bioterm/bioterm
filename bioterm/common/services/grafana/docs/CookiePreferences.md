# CookiePreferences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics** | **object** |  | [optional] 
**functional** | **object** |  | [optional] 
**performance** | **object** |  | [optional] 

## Example

```python
from grafanaApiClient.models.cookie_preferences import CookiePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of CookiePreferences from a JSON string
cookie_preferences_instance = CookiePreferences.from_json(json)
# print the JSON string representation of the object
print CookiePreferences.to_json()

# convert the object into a dict
cookie_preferences_dict = cookie_preferences_instance.to_dict()
# create an instance of CookiePreferences from a dict
cookie_preferences_form_dict = cookie_preferences.from_dict(cookie_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


