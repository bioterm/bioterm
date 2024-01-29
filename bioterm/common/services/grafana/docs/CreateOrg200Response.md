# CreateOrg200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message Message of the created org. | 
**org_id** | **int** | ID Identifier of the created org. | 

## Example

```python
from grafanaApiClient.models.create_org200_response import CreateOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrg200Response from a JSON string
create_org200_response_instance = CreateOrg200Response.from_json(json)
# print the JSON string representation of the object
print CreateOrg200Response.to_json()

# convert the object into a dict
create_org200_response_dict = create_org200_response_instance.to_dict()
# create an instance of CreateOrg200Response from a dict
create_org200_response_form_dict = create_org200_response.from_dict(create_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


