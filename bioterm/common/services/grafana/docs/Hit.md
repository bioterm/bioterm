# Hit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_title** | **str** |  | [optional] 
**folder_uid** | **str** |  | [optional] 
**folder_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_starred** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 
**sort_meta** | **int** |  | [optional] 
**sort_meta_name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.hit import Hit

# TODO update the JSON string below
json = "{}"
# create an instance of Hit from a JSON string
hit_instance = Hit.from_json(json)
# print the JSON string representation of the object
print Hit.to_json()

# convert the object into a dict
hit_dict = hit_instance.to_dict()
# create an instance of Hit from a dict
hit_form_dict = hit.from_dict(hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


