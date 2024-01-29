# AccessDeniedChallenge

Challenge when a flow's active stage calls `stage_invalid()`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-access-denied']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**error_message** | **str** |  | [optional] 

## Example

```python
from authentikApiClient.models.access_denied_challenge import AccessDeniedChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AccessDeniedChallenge from a JSON string
access_denied_challenge_instance = AccessDeniedChallenge.from_json(json)
# print the JSON string representation of the object
print AccessDeniedChallenge.to_json()

# convert the object into a dict
access_denied_challenge_dict = access_denied_challenge_instance.to_dict()
# create an instance of AccessDeniedChallenge from a dict
access_denied_challenge_form_dict = access_denied_challenge.from_dict(access_denied_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


