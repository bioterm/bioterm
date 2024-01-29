# RadiusProviderRequest

RadiusProvider Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**client_networks** | **str** | List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped. | [optional] 
**shared_secret** | **str** | Shared secret between clients and server to hash packets. | [optional] 

## Example

```python
from authentikApiClient.models.radius_provider_request import RadiusProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusProviderRequest from a JSON string
radius_provider_request_instance = RadiusProviderRequest.from_json(json)
# print the JSON string representation of the object
print RadiusProviderRequest.to_json()

# convert the object into a dict
radius_provider_request_dict = radius_provider_request_instance.to_dict()
# create an instance of RadiusProviderRequest from a dict
radius_provider_request_form_dict = radius_provider_request.from_dict(radius_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


