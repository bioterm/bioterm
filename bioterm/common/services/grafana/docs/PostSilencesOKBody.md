# PostSilencesOKBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**silence_id** | **str** | silence ID | [optional] 

## Example

```python
from grafanaApiClient.models.post_silences_ok_body import PostSilencesOKBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostSilencesOKBody from a JSON string
post_silences_ok_body_instance = PostSilencesOKBody.from_json(json)
# print the JSON string representation of the object
print PostSilencesOKBody.to_json()

# convert the object into a dict
post_silences_ok_body_dict = post_silences_ok_body_instance.to_dict()
# create an instance of PostSilencesOKBody from a dict
post_silences_ok_body_form_dict = post_silences_ok_body.from_dict(post_silences_ok_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


