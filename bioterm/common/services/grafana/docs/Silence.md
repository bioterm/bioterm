# Silence

Silence silence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | comment | 
**created_by** | **str** | created by | 
**ends_at** | **datetime** | ends at | 
**matchers** | [**List[Matcher]**](Matcher.md) | Matchers matchers | 
**starts_at** | **datetime** | starts at | 

## Example

```python
from grafanaApiClient.models.silence import Silence

# TODO update the JSON string below
json = "{}"
# create an instance of Silence from a JSON string
silence_instance = Silence.from_json(json)
# print the JSON string representation of the object
print Silence.to_json()

# convert the object into a dict
silence_dict = silence_instance.to_dict()
# create an instance of Silence from a dict
silence_form_dict = silence.from_dict(silence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


