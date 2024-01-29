# CreateQueryInQueryHistoryCommand

CreateQueryInQueryHistoryCommand is the command for adding query history

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_uid** | **str** | UID of the data source for which are queries stored. | [optional] 
**queries** | **object** |  | 

## Example

```python
from grafanaApiClient.models.create_query_in_query_history_command import CreateQueryInQueryHistoryCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQueryInQueryHistoryCommand from a JSON string
create_query_in_query_history_command_instance = CreateQueryInQueryHistoryCommand.from_json(json)
# print the JSON string representation of the object
print CreateQueryInQueryHistoryCommand.to_json()

# convert the object into a dict
create_query_in_query_history_command_dict = create_query_in_query_history_command_instance.to_dict()
# create an instance of CreateQueryInQueryHistoryCommand from a dict
create_query_in_query_history_command_form_dict = create_query_in_query_history_command.from_dict(create_query_in_query_history_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


