# Matcher

Matcher matcher

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_equal** | **bool** | is equal | [optional] 
**is_regex** | **bool** | is regex | 
**name** | **str** | name | 
**value** | **str** | value | 

## Example

```python
from grafanaApiClient.models.matcher import Matcher

# TODO update the JSON string below
json = "{}"
# create an instance of Matcher from a JSON string
matcher_instance = Matcher.from_json(json)
# print the JSON string representation of the object
print Matcher.to_json()

# convert the object into a dict
matcher_dict = matcher_instance.to_dict()
# create an instance of Matcher from a dict
matcher_form_dict = matcher.from_dict(matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


