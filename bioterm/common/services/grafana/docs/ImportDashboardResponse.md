# ImportDashboardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** |  | [optional] 
**imported** | **bool** |  | [optional] 
**imported_revision** | **int** |  | [optional] 
**imported_uri** | **str** |  | [optional] 
**imported_url** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 
**removed** | **bool** |  | [optional] 
**revision** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.import_dashboard_response import ImportDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDashboardResponse from a JSON string
import_dashboard_response_instance = ImportDashboardResponse.from_json(json)
# print the JSON string representation of the object
print ImportDashboardResponse.to_json()

# convert the object into a dict
import_dashboard_response_dict = import_dashboard_response_instance.to_dict()
# create an instance of ImportDashboardResponse from a dict
import_dashboard_response_form_dict = import_dashboard_response.from_dict(import_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


