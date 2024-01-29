# EvalQueriesPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | [optional] 
**now** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.eval_queries_payload import EvalQueriesPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EvalQueriesPayload from a JSON string
eval_queries_payload_instance = EvalQueriesPayload.from_json(json)
# print the JSON string representation of the object
print EvalQueriesPayload.to_json()

# convert the object into a dict
eval_queries_payload_dict = eval_queries_payload_instance.to_dict()
# create an instance of EvalQueriesPayload from a dict
eval_queries_payload_form_dict = eval_queries_payload.from_dict(eval_queries_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


