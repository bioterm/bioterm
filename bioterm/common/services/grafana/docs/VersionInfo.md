# VersionInfo

VersionInfo version info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | branch | 
**build_date** | **str** | build date | 
**build_user** | **str** | build user | 
**go_version** | **str** | go version | 
**revision** | **str** | revision | 
**version** | **str** | version | 

## Example

```python
from grafanaApiClient.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print VersionInfo.to_json()

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_form_dict = version_info.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


