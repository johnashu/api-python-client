# Check

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the check. Read-only. | [optional] 
**created_at** | **datetime** | The date and time when this check was created. Read-only. | [optional] 
**href** | **str** | The uri of this resource. Read-only. | [optional] 
**status** | **str** | The current state of the check in the checking process. Read-only. | [optional] 
**result** | **str** | The overall result of the check, based on the results of the constituent reports. Read-only. | [optional] 
**download_uri** | **str** | A link to a PDF output of the check results. Append &#x60;.pdf&#x60; to get the pdf file. Read-only. | [optional] 
**form_uri** | **str** | A link to the applicant form, if &#x60;applicant_provides_data&#x60; is &#x60;true&#x60;. Read-only. | [optional] 
**redirect_uri** | **str** | For checks where &#x60;applicant_provides_data&#x60; is &#x60;true&#x60;, redirect to this URI when the applicant has submitted their data. Read-only. | [optional] 
**results_uri** | **str** | A link to the corresponding results page on the Onfido dashboard. | [optional] 
**report_names** | **list[str]** | An array of report names (strings). | [optional] 
**applicant_id** | **str** | The ID of the applicant to do the check on. | [optional] 
**tags** | **list[str]** | Array of tags being assigned to this check. | [optional] 
**applicant_provides_data** | **bool** | Send an applicant form to applicant to complete to proceed with check. Defaults to false.  | [optional] 
**suppress_form_emails** | **bool** | For checks where &#x60;applicant_provides_data&#x60; is &#x60;true&#x60;, applicant form will not be automatically sent if &#x60;suppress_form_emails&#x60; is set to &#x60;true&#x60;. You can manually send the form at any time after the check has been created, using the link found in the form_uri attribute of the check object. Write-only. Defaults to false.  | [optional] 
**asynchronous** | **bool** | Defaults to &#x60;true&#x60;. Write-only. If set to &#x60;false&#x60;, you will only receive a response when all reports in your check have completed.  | [optional] 
**report_ids** | **list[str]** | An array of report ids. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


