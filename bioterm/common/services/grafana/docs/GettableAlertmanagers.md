# GettableAlertmanagers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlertManagersResult**](AlertManagersResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_alertmanagers import GettableAlertmanagers

# TODO update the JSON string below
json = "{}"
# create an instance of GettableAlertmanagers from a JSON string
gettable_alertmanagers_instance = GettableAlertmanagers.from_json(json)
# print the JSON string representation of the object
print GettableAlertmanagers.to_json()

# convert the object into a dict
gettable_alertmanagers_dict = gettable_alertmanagers_instance.to_dict()
# create an instance of GettableAlertmanagers from a dict
gettable_alertmanagers_form_dict = gettable_alertmanagers.from_dict(gettable_alertmanagers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


