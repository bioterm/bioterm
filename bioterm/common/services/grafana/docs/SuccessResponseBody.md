# SuccessResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.success_response_body import SuccessResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResponseBody from a JSON string
success_response_body_instance = SuccessResponseBody.from_json(json)
# print the JSON string representation of the object
print SuccessResponseBody.to_json()

# convert the object into a dict
success_response_body_dict = success_response_body_instance.to_dict()
# create an instance of SuccessResponseBody from a dict
success_response_body_form_dict = success_response_body.from_dict(success_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


