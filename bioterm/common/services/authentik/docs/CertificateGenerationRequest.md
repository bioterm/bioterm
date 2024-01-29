# CertificateGenerationRequest

Certificate generation parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** |  | 
**subject_alt_name** | **str** |  | [optional] 
**validity_days** | **int** |  | 

## Example

```python
from authentikApiClient.models.certificate_generation_request import CertificateGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateGenerationRequest from a JSON string
certificate_generation_request_instance = CertificateGenerationRequest.from_json(json)
# print the JSON string representation of the object
print CertificateGenerationRequest.to_json()

# convert the object into a dict
certificate_generation_request_dict = certificate_generation_request_instance.to_dict()
# create an instance of CertificateGenerationRequest from a dict
certificate_generation_request_form_dict = certificate_generation_request.from_dict(certificate_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


