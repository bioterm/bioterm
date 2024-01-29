# BrandingOptionsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_footer_link** | **str** |  | [optional] 
**email_footer_mode** | **str** |  | [optional] 
**email_footer_text** | **str** |  | [optional] 
**email_logo_url** | **str** |  | [optional] 
**report_logo_url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.branding_options_dto import BrandingOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingOptionsDTO from a JSON string
branding_options_dto_instance = BrandingOptionsDTO.from_json(json)
# print the JSON string representation of the object
print BrandingOptionsDTO.to_json()

# convert the object into a dict
branding_options_dto_dict = branding_options_dto_instance.to_dict()
# create an instance of BrandingOptionsDTO from a dict
branding_options_dto_form_dict = branding_options_dto.from_dict(branding_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


