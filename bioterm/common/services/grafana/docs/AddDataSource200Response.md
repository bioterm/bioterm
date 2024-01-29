# AddDataSource200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource** | [**DataSource**](DataSource.md) |  | 
**id** | **int** | ID Identifier of the new data source. | 
**message** | **str** | Message Message of the deleted dashboard. | 
**name** | **str** | Name of the new data source. | 

## Example

```python
from grafanaApiClient.models.add_data_source200_response import AddDataSource200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddDataSource200Response from a JSON string
add_data_source200_response_instance = AddDataSource200Response.from_json(json)
# print the JSON string representation of the object
print AddDataSource200Response.to_json()

# convert the object into a dict
add_data_source200_response_dict = add_data_source200_response_instance.to_dict()
# create an instance of AddDataSource200Response from a dict
add_data_source200_response_form_dict = add_data_source200_response.from_dict(add_data_source200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


