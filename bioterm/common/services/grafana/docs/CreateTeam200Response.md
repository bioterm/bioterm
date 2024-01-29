# CreateTeam200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_team200_response import CreateTeam200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeam200Response from a JSON string
create_team200_response_instance = CreateTeam200Response.from_json(json)
# print the JSON string representation of the object
print CreateTeam200Response.to_json()

# convert the object into a dict
create_team200_response_dict = create_team200_response_instance.to_dict()
# create an instance of CreateTeam200Response from a dict
create_team200_response_form_dict = create_team200_response.from_dict(create_team200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


