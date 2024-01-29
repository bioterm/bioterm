# GettableSilence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | comment | 
**created_by** | **str** | created by | 
**ends_at** | **datetime** | ends at | 
**id** | **str** | id | 
**matchers** | [**List[Matcher]**](Matcher.md) | Matchers matchers | 
**starts_at** | **datetime** | starts at | 
**status** | [**SilenceStatus**](SilenceStatus.md) |  | 
**updated_at** | **datetime** | updated at | 

## Example

```python
from grafanaApiClient.models.gettable_silence import GettableSilence

# TODO update the JSON string below
json = "{}"
# create an instance of GettableSilence from a JSON string
gettable_silence_instance = GettableSilence.from_json(json)
# print the JSON string representation of the object
print GettableSilence.to_json()

# convert the object into a dict
gettable_silence_dict = gettable_silence_instance.to_dict()
# create an instance of GettableSilence from a dict
gettable_silence_form_dict = gettable_silence.from_dict(gettable_silence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


