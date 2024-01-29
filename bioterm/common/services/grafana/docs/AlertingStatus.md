# AlertingStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertmanagers_choice** | **str** |  | [optional] 
**num_external_alertmanagers** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alerting_status import AlertingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingStatus from a JSON string
alerting_status_instance = AlertingStatus.from_json(json)
# print the JSON string representation of the object
print AlertingStatus.to_json()

# convert the object into a dict
alerting_status_dict = alerting_status_instance.to_dict()
# create an instance of AlertingStatus from a dict
alerting_status_form_dict = alerting_status.from_dict(alerting_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


