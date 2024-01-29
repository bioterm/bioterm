# RecordingRuleJSON

RecordingRuleJSON is the external representation of a recording rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**count** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**dest_data_source_uid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**interval** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prom_name** | **str** |  | [optional] 
**queries** | **List[object]** |  | [optional] 
**range** | **int** |  | [optional] 
**target_ref_id** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.recording_rule_json import RecordingRuleJSON

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingRuleJSON from a JSON string
recording_rule_json_instance = RecordingRuleJSON.from_json(json)
# print the JSON string representation of the object
print RecordingRuleJSON.to_json()

# convert the object into a dict
recording_rule_json_dict = recording_rule_json_instance.to_dict()
# create an instance of RecordingRuleJSON from a dict
recording_rule_json_form_dict = recording_rule_json.from_dict(recording_rule_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


