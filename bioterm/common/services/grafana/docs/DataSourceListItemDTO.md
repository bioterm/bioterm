# DataSourceListItemDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [optional] 
**basic_auth** | **bool** |  | [optional] 
**database** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**json_data** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**type_logo_url** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.data_source_list_item_dto import DataSourceListItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DataSourceListItemDTO from a JSON string
data_source_list_item_dto_instance = DataSourceListItemDTO.from_json(json)
# print the JSON string representation of the object
print DataSourceListItemDTO.to_json()

# convert the object into a dict
data_source_list_item_dto_dict = data_source_list_item_dto_instance.to_dict()
# create an instance of DataSourceListItemDTO from a dict
data_source_list_item_dto_form_dict = data_source_list_item_dto.from_dict(data_source_list_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


