# EmailConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_identity** | **str** |  | [optional] 
**auth_password** | **str** |  | [optional] 
**auth_password_file** | **str** |  | [optional] 
**auth_secret** | **str** |  | [optional] 
**auth_username** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**hello** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**require_tls** | **bool** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**smarthost** | [**HostPort**](HostPort.md) |  | [optional] 
**text** | **str** |  | [optional] 
**tls_config** | [**TLSConfig**](TLSConfig.md) |  | [optional] 
**to** | **str** | Email address to notify. | [optional] 

## Example

```python
from grafanaApiClient.models.email_config import EmailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfig from a JSON string
email_config_instance = EmailConfig.from_json(json)
# print the JSON string representation of the object
print EmailConfig.to_json()

# convert the object into a dict
email_config_dict = email_config_instance.to_dict()
# create an instance of EmailConfig from a dict
email_config_form_dict = email_config.from_dict(email_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


