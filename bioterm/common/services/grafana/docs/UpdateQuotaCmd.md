# UpdateQuotaCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_quota_cmd import UpdateQuotaCmd

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuotaCmd from a JSON string
update_quota_cmd_instance = UpdateQuotaCmd.from_json(json)
# print the JSON string representation of the object
print UpdateQuotaCmd.to_json()

# convert the object into a dict
update_quota_cmd_dict = update_quota_cmd_instance.to_dict()
# create an instance of UpdateQuotaCmd from a dict
update_quota_cmd_form_dict = update_quota_cmd.from_dict(update_quota_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


