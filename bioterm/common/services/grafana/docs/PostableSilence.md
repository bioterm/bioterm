# PostableSilence

PostableSilence postable silence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | comment | 
**created_by** | **str** | created by | 
**ends_at** | **datetime** | ends at | 
**id** | **str** | id | [optional] 
**matchers** | [**List[Matcher]**](Matcher.md) | Matchers matchers | 
**starts_at** | **datetime** | starts at | 

## Example

```python
from grafanaApiClient.models.postable_silence import PostableSilence

# TODO update the JSON string below
json = "{}"
# create an instance of PostableSilence from a JSON string
postable_silence_instance = PostableSilence.from_json(json)
# print the JSON string representation of the object
print PostableSilence.to_json()

# convert the object into a dict
postable_silence_dict = postable_silence_instance.to_dict()
# create an instance of PostableSilence from a dict
postable_silence_form_dict = postable_silence.from_dict(postable_silence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


