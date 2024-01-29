# PauseAlert200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | 
**message** | **str** |  | 
**state** | **str** | Alert result state required true | [optional] 

## Example

```python
from grafanaApiClient.models.pause_alert200_response import PauseAlert200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PauseAlert200Response from a JSON string
pause_alert200_response_instance = PauseAlert200Response.from_json(json)
# print the JSON string representation of the object
print PauseAlert200Response.to_json()

# convert the object into a dict
pause_alert200_response_dict = pause_alert200_response_instance.to_dict()
# create an instance of PauseAlert200Response from a dict
pause_alert200_response_form_dict = pause_alert200_response.from_dict(pause_alert200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


