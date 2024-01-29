# GetSharingOptions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_enabled** | **bool** |  | [optional] 
**external_snapshot_name** | **str** |  | [optional] 
**external_snapshot_url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.get_sharing_options200_response import GetSharingOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSharingOptions200Response from a JSON string
get_sharing_options200_response_instance = GetSharingOptions200Response.from_json(json)
# print the JSON string representation of the object
print GetSharingOptions200Response.to_json()

# convert the object into a dict
get_sharing_options200_response_dict = get_sharing_options200_response_instance.to_dict()
# create an instance of GetSharingOptions200Response from a dict
get_sharing_options200_response_form_dict = get_sharing_options200_response.from_dict(get_sharing_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


