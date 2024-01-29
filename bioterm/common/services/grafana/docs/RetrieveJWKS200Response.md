# RetrieveJWKS200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[JSONWebKey]**](JSONWebKey.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.retrieve_jwks200_response import RetrieveJWKS200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveJWKS200Response from a JSON string
retrieve_jwks200_response_instance = RetrieveJWKS200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveJWKS200Response.to_json()

# convert the object into a dict
retrieve_jwks200_response_dict = retrieve_jwks200_response_instance.to_dict()
# create an instance of RetrieveJWKS200Response from a dict
retrieve_jwks200_response_form_dict = retrieve_jwks200_response.from_dict(retrieve_jwks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


