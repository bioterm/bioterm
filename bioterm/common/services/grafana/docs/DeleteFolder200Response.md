# DeleteFolder200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID Identifier of the deleted folder. | 
**message** | **str** | Message Message of the deleted folder. | 
**title** | **str** | Title of the deleted folder. | 

## Example

```python
from grafanaApiClient.models.delete_folder200_response import DeleteFolder200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFolder200Response from a JSON string
delete_folder200_response_instance = DeleteFolder200Response.from_json(json)
# print the JSON string representation of the object
print DeleteFolder200Response.to_json()

# convert the object into a dict
delete_folder200_response_dict = delete_folder200_response_instance.to_dict()
# create an instance of DeleteFolder200Response from a dict
delete_folder200_response_form_dict = delete_folder200_response.from_dict(delete_folder200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


