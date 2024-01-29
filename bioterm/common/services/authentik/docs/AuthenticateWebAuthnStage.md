# AuthenticateWebAuthnStage

AuthenticateWebAuthnStage Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**authenticator_attachment** | [**AuthenticatorAttachmentEnum**](AuthenticatorAttachmentEnum.md) |  | [optional] 
**resident_key_requirement** | [**ResidentKeyRequirementEnum**](ResidentKeyRequirementEnum.md) |  | [optional] 

## Example

```python
from authentikApiClient.models.authenticate_web_authn_stage import AuthenticateWebAuthnStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateWebAuthnStage from a JSON string
authenticate_web_authn_stage_instance = AuthenticateWebAuthnStage.from_json(json)
# print the JSON string representation of the object
print AuthenticateWebAuthnStage.to_json()

# convert the object into a dict
authenticate_web_authn_stage_dict = authenticate_web_authn_stage_instance.to_dict()
# create an instance of AuthenticateWebAuthnStage from a dict
authenticate_web_authn_stage_form_dict = authenticate_web_authn_stage.from_dict(authenticate_web_authn_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


