# PatchQueryCommentInQueryHistoryCommand

PatchQueryCommentInQueryHistoryCommand is the command for updating comment for query in query history

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Updated comment | [optional] 

## Example

```python
from grafanaApiClient.models.patch_query_comment_in_query_history_command import PatchQueryCommentInQueryHistoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PatchQueryCommentInQueryHistoryCommand from a JSON string
patch_query_comment_in_query_history_command_instance = PatchQueryCommentInQueryHistoryCommand.from_json(json)
# print the JSON string representation of the object
print PatchQueryCommentInQueryHistoryCommand.to_json()

# convert the object into a dict
patch_query_comment_in_query_history_command_dict = patch_query_comment_in_query_history_command_instance.to_dict()
# create an instance of PatchQueryCommentInQueryHistoryCommand from a dict
patch_query_comment_in_query_history_command_form_dict = patch_query_comment_in_query_history_command.from_dict(patch_query_comment_in_query_history_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


