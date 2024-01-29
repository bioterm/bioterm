# QueryDataResponse

It is the return type of a QueryData call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**Dict[str, DataResponse]**](DataResponse.md) | The QueryData method the QueryDataHandler method will set the RefId property on the DataResponses&#39; frames based on these RefIDs. | [optional] 

## Example

```python
from grafanaApiClient.models.query_data_response import QueryDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDataResponse from a JSON string
query_data_response_instance = QueryDataResponse.from_json(json)
# print the JSON string representation of the object
print QueryDataResponse.to_json()

# convert the object into a dict
query_data_response_dict = query_data_response_instance.to_dict()
# create an instance of QueryDataResponse from a dict
query_data_response_form_dict = query_data_response.from_dict(query_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


