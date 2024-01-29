# PrometheusRemoteWriteTargetJSON


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source_uid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**remote_write_path** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.prometheus_remote_write_target_json import PrometheusRemoteWriteTargetJSON

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusRemoteWriteTargetJSON from a JSON string
prometheus_remote_write_target_json_instance = PrometheusRemoteWriteTargetJSON.from_json(json)
# print the JSON string representation of the object
print PrometheusRemoteWriteTargetJSON.to_json()

# convert the object into a dict
prometheus_remote_write_target_json_dict = prometheus_remote_write_target_json_instance.to_dict()
# create an instance of PrometheusRemoteWriteTargetJSON from a dict
prometheus_remote_write_target_json_form_dict = prometheus_remote_write_target_json.from_dict(prometheus_remote_write_target_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


