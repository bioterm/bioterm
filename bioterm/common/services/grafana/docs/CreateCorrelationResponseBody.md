# CreateCorrelationResponseBody

CreateCorrelationResponse is the response struct for CreateCorrelationCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**Correlation**](Correlation.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_correlation_response_body import CreateCorrelationResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCorrelationResponseBody from a JSON string
create_correlation_response_body_instance = CreateCorrelationResponseBody.from_json(json)
# print the JSON string representation of the object
print CreateCorrelationResponseBody.to_json()

# convert the object into a dict
create_correlation_response_body_dict = create_correlation_response_body_instance.to_dict()
# create an instance of CreateCorrelationResponseBody from a dict
create_correlation_response_body_form_dict = create_correlation_response_body.from_dict(create_correlation_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


