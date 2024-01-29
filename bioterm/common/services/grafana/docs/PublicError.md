# PublicError

PublicError is derived from Error and only contains information available to the end user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **object** | Extra Additional information about the error | [optional] 
**message** | **str** | Message A human readable message | [optional] 
**message_id** | **str** | MessageID A unique identifier for the error | 
**status_code** | **int** | StatusCode The HTTP status code returned | 

## Example

```python
from grafanaApiClient.models.public_error import PublicError

# TODO update the JSON string below
json = "{}"
# create an instance of PublicError from a JSON string
public_error_instance = PublicError.from_json(json)
# print the JSON string representation of the object
print PublicError.to_json()

# convert the object into a dict
public_error_dict = public_error_instance.to_dict()
# create an instance of PublicError from a dict
public_error_form_dict = public_error.from_dict(public_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


