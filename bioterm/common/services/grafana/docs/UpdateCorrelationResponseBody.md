# UpdateCorrelationResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**Correlation**](Correlation.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_correlation_response_body import UpdateCorrelationResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCorrelationResponseBody from a JSON string
update_correlation_response_body_instance = UpdateCorrelationResponseBody.from_json(json)
# print the JSON string representation of the object
print UpdateCorrelationResponseBody.to_json()

# convert the object into a dict
update_correlation_response_body_dict = update_correlation_response_body_instance.to_dict()
# create an instance of UpdateCorrelationResponseBody from a dict
update_correlation_response_body_form_dict = update_correlation_response_body.from_dict(update_correlation_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


