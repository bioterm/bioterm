# AlertResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AlertDiscovery**](AlertDiscovery.md) |  | [optional] 
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from grafanaApiClient.models.alert_response import AlertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResponse from a JSON string
alert_response_instance = AlertResponse.from_json(json)
# print the JSON string representation of the object
print AlertResponse.to_json()

# convert the object into a dict
alert_response_dict = alert_response_instance.to_dict()
# create an instance of AlertResponse from a dict
alert_response_form_dict = alert_response.from_dict(alert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


