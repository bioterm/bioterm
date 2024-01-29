# FailedUser

FailedUser holds the information of an user that failed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**login** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.failed_user import FailedUser

# TODO update the JSON string below
json = "{}"
# create an instance of FailedUser from a JSON string
failed_user_instance = FailedUser.from_json(json)
# print the JSON string representation of the object
print FailedUser.to_json()

# convert the object into a dict
failed_user_dict = failed_user_instance.to_dict()
# create an instance of FailedUser from a dict
failed_user_form_dict = failed_user.from_dict(failed_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


