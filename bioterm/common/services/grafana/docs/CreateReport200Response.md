# CreateReport200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_report200_response import CreateReport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReport200Response from a JSON string
create_report200_response_instance = CreateReport200Response.from_json(json)
# print the JSON string representation of the object
print CreateReport200Response.to_json()

# convert the object into a dict
create_report200_response_dict = create_report200_response_instance.to_dict()
# create an instance of CreateReport200Response from a dict
create_report200_response_form_dict = create_report200_response.from_dict(create_report200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


