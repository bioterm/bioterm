# PagerdutyLink

PagerdutyLink is a link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.pagerduty_link import PagerdutyLink

# TODO update the JSON string below
json = "{}"
# create an instance of PagerdutyLink from a JSON string
pagerduty_link_instance = PagerdutyLink.from_json(json)
# print the JSON string representation of the object
print PagerdutyLink.to_json()

# convert the object into a dict
pagerduty_link_dict = pagerduty_link_instance.to_dict()
# create an instance of PagerdutyLink from a dict
pagerduty_link_form_dict = pagerduty_link.from_dict(pagerduty_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


