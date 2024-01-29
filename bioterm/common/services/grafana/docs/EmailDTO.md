# EmailDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.email_dto import EmailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDTO from a JSON string
email_dto_instance = EmailDTO.from_json(json)
# print the JSON string representation of the object
print EmailDTO.to_json()

# convert the object into a dict
email_dto_dict = email_dto_instance.to_dict()
# create an instance of EmailDTO from a dict
email_dto_form_dict = email_dto.from_dict(email_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


