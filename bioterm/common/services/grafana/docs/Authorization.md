# Authorization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **str** |  | [optional] 
**credentials_file** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.authorization import Authorization

# TODO update the JSON string below
json = "{}"
# create an instance of Authorization from a JSON string
authorization_instance = Authorization.from_json(json)
# print the JSON string representation of the object
print Authorization.to_json()

# convert the object into a dict
authorization_dict = authorization_instance.to_dict()
# create an instance of Authorization from a dict
authorization_form_dict = authorization.from_dict(authorization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


