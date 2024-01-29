# Folder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **Dict[str, bool]** | Metadata contains user accesses for a given resource Ex: map[string]bool{\&quot;create\&quot;:true, \&quot;delete\&quot;: true} | [optional] 
**can_admin** | **bool** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**can_edit** | **bool** |  | [optional] 
**can_save** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**has_acl** | **bool** |  | [optional] 
**id** | **int** | Deprecated: use Uid instead | [optional] 
**parent_uid** | **str** | only used if nested folders are enabled | [optional] 
**parents** | [**List[Folder]**](Folder.md) | the parent folders starting from the root going down | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print Folder.to_json()

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_form_dict = folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


