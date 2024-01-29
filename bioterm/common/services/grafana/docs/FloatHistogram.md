# FloatHistogram

A FloatHistogram is needed by PromQL to handle operations that might result in fractional counts. Since the counts in a histogram are unlikely to be too large to be represented precisely by a float64, a FloatHistogram can also be used to represent a histogram with integer counts and thus serves as a more generalized representation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** | Total number of observations. Must be zero or positive. | [optional] 
**counter_reset_hint** | **int** | or alternatively that we are dealing with a gauge histogram, where counter resets do not apply. | [optional] 
**positive_buckets** | **List[float]** | Observation counts in buckets. Each represents an absolute count and must be zero or positive. | [optional] 
**positive_spans** | [**List[Span]**](Span.md) | Spans for positive and negative buckets (see Span below). | [optional] 
**var_schema** | **int** | Currently valid schema numbers are -4 &lt;&#x3D; n &lt;&#x3D; 8.  They are all for base-2 bucket schemas, where 1 is a bucket boundary in each case, and then each power of two is divided into 2^n logarithmic buckets.  Or in other words, each bucket boundary is the previous boundary times 2^(2^-n). | [optional] 
**sum** | **float** | Sum of observations. This is also used as the stale marker. | [optional] 
**zero_count** | **float** | Observations falling into the zero bucket. Must be zero or positive. | [optional] 
**zero_threshold** | **float** | Width of the zero bucket. | [optional] 

## Example

```python
from grafanaApiClient.models.float_histogram import FloatHistogram

# TODO update the JSON string below
json = "{}"
# create an instance of FloatHistogram from a JSON string
float_histogram_instance = FloatHistogram.from_json(json)
# print the JSON string representation of the object
print FloatHistogram.to_json()

# convert the object into a dict
float_histogram_dict = float_histogram_instance.to_dict()
# create an instance of FloatHistogram from a dict
float_histogram_form_dict = float_histogram.from_dict(float_histogram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


