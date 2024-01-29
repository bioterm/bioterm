# DeleteDataSourceByName200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID Identifier of the deleted data source. | 
**message** | **str** | Message Message of the deleted dashboard. | 

## Example

```python
from grafanaApiClient.models.delete_data_source_by_name200_response import DeleteDataSourceByName200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDataSourceByName200Response from a JSON string
delete_data_source_by_name200_response_instance = DeleteDataSourceByName200Response.from_json(json)
# print the JSON string representation of the object
print DeleteDataSourceByName200Response.to_json()

# convert the object into a dict
delete_data_source_by_name200_response_dict = delete_data_source_by_name200_response_instance.to_dict()
# create an instance of DeleteDataSourceByName200Response from a dict
delete_data_source_by_name200_response_form_dict = delete_data_source_by_name200_response.from_dict(delete_data_source_by_name200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


