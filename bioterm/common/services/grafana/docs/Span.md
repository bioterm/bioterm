# Span


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Length of the span. | [optional] 
**offset** | **int** | Gap to previous span (always positive), or starting index for the 1st span (which can be negative). | [optional] 

## Example

```python
from grafanaApiClient.models.span import Span

# TODO update the JSON string below
json = "{}"
# create an instance of Span from a JSON string
span_instance = Span.from_json(json)
# print the JSON string representation of the object
print Span.to_json()

# convert the object into a dict
span_dict = span_instance.to_dict()
# create an instance of Span from a dict
span_form_dict = span.from_dict(span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


