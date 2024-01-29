# PagerdutyImage

PagerdutyImage is an image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**src** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.pagerduty_image import PagerdutyImage

# TODO update the JSON string below
json = "{}"
# create an instance of PagerdutyImage from a JSON string
pagerduty_image_instance = PagerdutyImage.from_json(json)
# print the JSON string representation of the object
print PagerdutyImage.to_json()

# convert the object into a dict
pagerduty_image_dict = pagerduty_image_instance.to_dict()
# create an instance of PagerdutyImage from a dict
pagerduty_image_form_dict = pagerduty_image.from_dict(pagerduty_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


