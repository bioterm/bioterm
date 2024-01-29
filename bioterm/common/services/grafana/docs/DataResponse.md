# DataResponse

A map of RefIDs (unique query identifiers) to this type makes up the Responses property of a QueryDataResponse. The Error property is used to allow for partial success responses from the containing QueryDataResponse.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error is a property to be set if the corresponding DataQuery has an error. | [optional] 
**error_source** | **str** | ErrorSource type defines the source of the error | [optional] 
**frames** | [**List[Frame]**](Frame.md) | It is the main data container within a backend.DataResponse. There should be no &#x60;nil&#x60; entries in the Frames slice (making them pointers was a mistake). | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.data_response import DataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataResponse from a JSON string
data_response_instance = DataResponse.from_json(json)
# print the JSON string representation of the object
print DataResponse.to_json()

# convert the object into a dict
data_response_dict = data_response_instance.to_dict()
# create an instance of DataResponse from a dict
data_response_form_dict = data_response.from_dict(data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


