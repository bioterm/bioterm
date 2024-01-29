# Task

Serialize TaskInfo and TaskResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** |  | 
**task_description** | **str** |  | 
**task_finish_timestamp** | **datetime** |  | 
**task_duration** | **int** | Get the duration a task took to run | [readonly] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) |  | 
**messages** | **List[object]** |  | 

## Example

```python
from authentikApiClient.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


