# EvalMatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | [optional] 
**tags** | **Dict[str, str]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.eval_match import EvalMatch

# TODO update the JSON string below
json = "{}"
# create an instance of EvalMatch from a JSON string
eval_match_instance = EvalMatch.from_json(json)
# print the JSON string representation of the object
print EvalMatch.to_json()

# convert the object into a dict
eval_match_dict = eval_match_instance.to_dict()
# create an instance of EvalMatch from a dict
eval_match_form_dict = eval_match.from_dict(eval_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


