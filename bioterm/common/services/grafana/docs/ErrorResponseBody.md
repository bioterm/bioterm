# ErrorResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error An optional detailed description of the actual error. Only included if running in developer mode. | [optional] 
**message** | **str** | a human readable version of the error | 
**status** | **str** | Status An optional status to denote the cause of the error.  For example, a 412 Precondition Failed error may include additional information of why that error happened. | [optional] 

## Example

```python
from grafanaApiClient.models.error_response_body import ErrorResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseBody from a JSON string
error_response_body_instance = ErrorResponseBody.from_json(json)
# print the JSON string representation of the object
print ErrorResponseBody.to_json()

# convert the object into a dict
error_response_body_dict = error_response_body_instance.to_dict()
# create an instance of ErrorResponseBody from a dict
error_response_body_form_dict = error_response_body.from_dict(error_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


