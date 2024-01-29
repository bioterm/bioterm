# JSONWebKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Key algorithm, parsed from &#x60;alg&#x60; header. | [optional] 
**certificate_thumbprint_sha1** | **List[int]** | X.509 certificate thumbprint (SHA-1), parsed from &#x60;x5t&#x60; header. | [optional] 
**certificate_thumbprint_sha256** | **List[int]** | X.509 certificate thumbprint (SHA-256), parsed from &#x60;x5t#S256&#x60; header. | [optional] 
**certificates** | [**List[Certificate]**](Certificate.md) | X.509 certificate chain, parsed from &#x60;x5c&#x60; header. | [optional] 
**certificates_url** | [**URL**](URL.md) |  | [optional] 
**key** | **object** | Cryptographic key, can be a symmetric or asymmetric key. | [optional] 
**key_id** | **str** | Key identifier, parsed from &#x60;kid&#x60; header. | [optional] 
**use** | **str** | Key use, parsed from &#x60;use&#x60; header. | [optional] 

## Example

```python
from grafanaApiClient.models.json_web_key import JSONWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of JSONWebKey from a JSON string
json_web_key_instance = JSONWebKey.from_json(json)
# print the JSON string representation of the object
print JSONWebKey.to_json()

# convert the object into a dict
json_web_key_dict = json_web_key_instance.to_dict()
# create an instance of JSONWebKey from a dict
json_web_key_form_dict = json_web_key.from_dict(json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


