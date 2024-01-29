# Route

A Route is a node that contains definitions of how to handle alerts. This is modified from the upstream alertmanager in that it adds the ObjectMatchers property.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_continue** | **bool** |  | [optional] 
**group_by** | **List[str]** |  | [optional] 
**group_interval** | **str** |  | [optional] 
**group_wait** | **str** |  | [optional] 
**match** | **Dict[str, str]** | Deprecated. Remove before v1.0 release. | [optional] 
**match_re** | **Dict[str, object]** |  | [optional] 
**matchers** | [**List[Matcher]**](Matcher.md) | Matchers is a slice of Matchers that is sortable, implements Stringer, and provides a Matches method to match a LabelSet against all Matchers in the slice. Note that some users of Matchers might require it to be sorted. | [optional] 
**mute_time_intervals** | **List[str]** |  | [optional] 
**object_matchers** | [**List[Matcher]**](Matcher.md) | Matchers is a slice of Matchers that is sortable, implements Stringer, and provides a Matches method to match a LabelSet against all Matchers in the slice. Note that some users of Matchers might require it to be sorted. | [optional] 
**provenance** | **str** |  | [optional] 
**receiver** | **str** |  | [optional] 
**repeat_interval** | **str** |  | [optional] 
**routes** | [**List[Route]**](Route.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print Route.to_json()

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_form_dict = route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


