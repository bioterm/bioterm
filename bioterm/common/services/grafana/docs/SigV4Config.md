# SigV4Config

SigV4Config is the configuration for signing remote write requests with AWS's SigV4 verification process. Empty values will be retrieved using the AWS default credentials chain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**role_arn** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.sig_v4_config import SigV4Config

# TODO update the JSON string below
json = "{}"
# create an instance of SigV4Config from a JSON string
sig_v4_config_instance = SigV4Config.from_json(json)
# print the JSON string representation of the object
print SigV4Config.to_json()

# convert the object into a dict
sig_v4_config_dict = sig_v4_config_instance.to_dict()
# create an instance of SigV4Config from a dict
sig_v4_config_form_dict = sig_v4_config.from_dict(sig_v4_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


