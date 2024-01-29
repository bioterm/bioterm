# DataSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [optional] 
**access_control** | **Dict[str, bool]** | Metadata contains user accesses for a given resource Ex: map[string]bool{\&quot;create\&quot;:true, \&quot;delete\&quot;: true} | [optional] 
**basic_auth** | **bool** |  | [optional] 
**basic_auth_user** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**json_data** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**secure_json_fields** | **Dict[str, bool]** |  | [optional] 
**type** | **str** |  | [optional] 
**type_logo_url** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**with_credentials** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.data_source import DataSource

# TODO update the JSON string below
json = "{}"
# create an instance of DataSource from a JSON string
data_source_instance = DataSource.from_json(json)
# print the JSON string representation of the object
print DataSource.to_json()

# convert the object into a dict
data_source_dict = data_source_instance.to_dict()
# create an instance of DataSource from a dict
data_source_form_dict = data_source.from_dict(data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


