# ImportDashboardRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | **object** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** |  | [optional] 
**inputs** | [**List[ImportDashboardInput]**](ImportDashboardInput.md) |  | [optional] 
**overwrite** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**plugin_id** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.import_dashboard_request import ImportDashboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportDashboardRequest from a JSON string
import_dashboard_request_instance = ImportDashboardRequest.from_json(json)
# print the JSON string representation of the object
print ImportDashboardRequest.to_json()

# convert the object into a dict
import_dashboard_request_dict = import_dashboard_request_instance.to_dict()
# create an instance of ImportDashboardRequest from a dict
import_dashboard_request_form_dict = import_dashboard_request.from_dict(import_dashboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


