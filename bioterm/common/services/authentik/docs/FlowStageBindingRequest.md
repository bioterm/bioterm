# FlowStageBindingRequest

FlowStageBinding Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | 
**stage** | **str** |  | 
**evaluate_on_plan** | **bool** | Evaluate policies during the Flow planning process. | [optional] 
**re_evaluate_policies** | **bool** | Evaluate policies when the Stage is present to the user. | [optional] 
**order** | **int** |  | 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**invalid_response_action** | [**InvalidResponseActionEnum**](InvalidResponseActionEnum.md) |  | [optional] 

## Example

```python
from authentikApiClient.models.flow_stage_binding_request import FlowStageBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowStageBindingRequest from a JSON string
flow_stage_binding_request_instance = FlowStageBindingRequest.from_json(json)
# print the JSON string representation of the object
print FlowStageBindingRequest.to_json()

# convert the object into a dict
flow_stage_binding_request_dict = flow_stage_binding_request_instance.to_dict()
# create an instance of FlowStageBindingRequest from a dict
flow_stage_binding_request_form_dict = flow_stage_binding_request.from_dict(flow_stage_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


