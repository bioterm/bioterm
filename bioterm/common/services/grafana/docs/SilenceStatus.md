# SilenceStatus

SilenceStatus silence status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | state | 

## Example

```python
from grafanaApiClient.models.silence_status import SilenceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SilenceStatus from a JSON string
silence_status_instance = SilenceStatus.from_json(json)
# print the JSON string representation of the object
print SilenceStatus.to_json()

# convert the object into a dict
silence_status_dict = silence_status_instance.to_dict()
# create an instance of SilenceStatus from a dict
silence_status_form_dict = silence_status.from_dict(silence_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


