# ResponseDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.response_details import ResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDetails from a JSON string
response_details_instance = ResponseDetails.from_json(json)
# print the JSON string representation of the object
print ResponseDetails.to_json()

# convert the object into a dict
response_details_dict = response_details_instance.to_dict()
# create an instance of ResponseDetails from a dict
response_details_form_dict = response_details.from_dict(response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


