# PostAnnotation200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID Identifier of the created annotation. | 
**message** | **str** | Message Message of the created annotation. | 

## Example

```python
from grafanaApiClient.models.post_annotation200_response import PostAnnotation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostAnnotation200Response from a JSON string
post_annotation200_response_instance = PostAnnotation200Response.from_json(json)
# print the JSON string representation of the object
print PostAnnotation200Response.to_json()

# convert the object into a dict
post_annotation200_response_dict = post_annotation200_response_instance.to_dict()
# create an instance of PostAnnotation200Response from a dict
post_annotation200_response_form_dict = post_annotation200_response.from_dict(post_annotation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


