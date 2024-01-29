# PauseAllAlerts200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts_affected** | **int** | AlertsAffected is the number of the affected alerts. | 
**message** | **str** |  | 
**state** | **str** | Alert result state required true | [optional] 

## Example

```python
from grafanaApiClient.models.pause_all_alerts200_response import PauseAllAlerts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PauseAllAlerts200Response from a JSON string
pause_all_alerts200_response_instance = PauseAllAlerts200Response.from_json(json)
# print the JSON string representation of the object
print PauseAllAlerts200Response.to_json()

# convert the object into a dict
pause_all_alerts200_response_dict = pause_all_alerts200_response_instance.to_dict()
# create an instance of PauseAllAlerts200Response from a dict
pause_all_alerts200_response_form_dict = pause_all_alerts200_response.from_dict(pause_all_alerts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


