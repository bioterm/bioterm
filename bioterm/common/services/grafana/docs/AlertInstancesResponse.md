# AlertInstancesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | **List[List[int]]** | Instances is an array of arrow encoded dataframes each frame has a single row, and a column for each instance (alert identified by unique labels) with a boolean value (firing/not firing) | [optional] 

## Example

```python
from grafanaApiClient.models.alert_instances_response import AlertInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertInstancesResponse from a JSON string
alert_instances_response_instance = AlertInstancesResponse.from_json(json)
# print the JSON string representation of the object
print AlertInstancesResponse.to_json()

# convert the object into a dict
alert_instances_response_dict = alert_instances_response_instance.to_dict()
# create an instance of AlertInstancesResponse from a dict
alert_instances_response_form_dict = alert_instances_response.from_dict(alert_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


