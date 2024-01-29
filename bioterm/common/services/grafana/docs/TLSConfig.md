# TLSConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Text of the CA cert to use for the targets. | [optional] 
**ca_file** | **str** | The CA cert to use for the targets. | [optional] 
**cert** | **str** | Text of the client cert file for the targets. | [optional] 
**cert_file** | **str** | The client cert file for the targets. | [optional] 
**insecure_skip_verify** | **bool** | Disable target certificate validation. | [optional] 
**key** | **str** |  | [optional] 
**key_file** | **str** | The client key file for the targets. | [optional] 
**max_version** | **int** |  | [optional] 
**min_version** | **int** |  | [optional] 
**server_name** | **str** | Used to verify the hostname for the targets. | [optional] 

## Example

```python
from grafanaApiClient.models.tls_config import TLSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TLSConfig from a JSON string
tls_config_instance = TLSConfig.from_json(json)
# print the JSON string representation of the object
print TLSConfig.to_json()

# convert the object into a dict
tls_config_dict = tls_config_instance.to_dict()
# create an instance of TLSConfig from a dict
tls_config_form_dict = tls_config.from_dict(tls_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


