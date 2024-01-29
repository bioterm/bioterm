# SettingsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding** | [**BrandingOptionsDTO**](BrandingOptionsDTO.md) |  | [optional] 
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.settings_dto import SettingsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsDTO from a JSON string
settings_dto_instance = SettingsDTO.from_json(json)
# print the JSON string representation of the object
print SettingsDTO.to_json()

# convert the object into a dict
settings_dto_dict = settings_dto_instance.to_dict()
# create an instance of SettingsDTO from a dict
settings_dto_form_dict = settings_dto.from_dict(settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


