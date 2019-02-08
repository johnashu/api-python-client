# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CheckCommon(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'created_at': 'datetime',
        'href': 'str',
        'status': 'str',
        'result': 'str',
        'download_uri': 'str',
        'form_uri': 'str',
        'redirect_uri': 'str',
        'results_uri': 'str',
        'type': 'str',
        'report_type_groups': 'list[str]',
        'tags': 'list[str]',
        'suppress_form_emails': 'bool',
        'charge_applicant_for_check': 'bool',
        'brand_id': 'str',
        'async': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'href': 'href',
        'status': 'status',
        'result': 'result',
        'download_uri': 'download_uri',
        'form_uri': 'form_uri',
        'redirect_uri': 'redirect_uri',
        'results_uri': 'results_uri',
        'type': 'type',
        'report_type_groups': 'report_type_groups',
        'tags': 'tags',
        'suppress_form_emails': 'suppress_form_emails',
        'charge_applicant_for_check': 'charge_applicant_for_check',
        'brand_id': 'brand_id',
        'async': 'async'
    }

    def __init__(self, id=None, created_at=None, href=None, status=None, result=None, download_uri=None, form_uri=None, redirect_uri=None, results_uri=None, type=None, report_type_groups=None, tags=None, suppress_form_emails=False, charge_applicant_for_check=False, brand_id=None, async=False):  # noqa: E501
        """CheckCommon - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._href = None
        self._status = None
        self._result = None
        self._download_uri = None
        self._form_uri = None
        self._redirect_uri = None
        self._results_uri = None
        self._type = None
        self._report_type_groups = None
        self._tags = None
        self._suppress_form_emails = None
        self._charge_applicant_for_check = None
        self._brand_id = None
        self._async = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if href is not None:
            self.href = href
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if download_uri is not None:
            self.download_uri = download_uri
        if form_uri is not None:
            self.form_uri = form_uri
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if results_uri is not None:
            self.results_uri = results_uri
        if type is not None:
            self.type = type
        if report_type_groups is not None:
            self.report_type_groups = report_type_groups
        if tags is not None:
            self.tags = tags
        if suppress_form_emails is not None:
            self.suppress_form_emails = suppress_form_emails
        if charge_applicant_for_check is not None:
            self.charge_applicant_for_check = charge_applicant_for_check
        if brand_id is not None:
            self.brand_id = brand_id
        if async is not None:
            self.async = async

    @property
    def id(self):
        """Gets the id of this CheckCommon.  # noqa: E501

        The unique identifier for the check. Read-only.  # noqa: E501

        :return: The id of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CheckCommon.

        The unique identifier for the check. Read-only.  # noqa: E501

        :param id: The id of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this CheckCommon.  # noqa: E501

        The date and time when this check was created. Read-only.  # noqa: E501

        :return: The created_at of this CheckCommon.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CheckCommon.

        The date and time when this check was created. Read-only.  # noqa: E501

        :param created_at: The created_at of this CheckCommon.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def href(self):
        """Gets the href of this CheckCommon.  # noqa: E501

        The uri of this resource. Read-only.  # noqa: E501

        :return: The href of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CheckCommon.

        The uri of this resource. Read-only.  # noqa: E501

        :param href: The href of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def status(self):
        """Gets the status of this CheckCommon.  # noqa: E501

        The current state of the check in the checking process. Read-only.  # noqa: E501

        :return: The status of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckCommon.

        The current state of the check in the checking process. Read-only.  # noqa: E501

        :param status: The status of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def result(self):
        """Gets the result of this CheckCommon.  # noqa: E501

        The overall result of the check, based on the results of the constituent reports. Read-only.  # noqa: E501

        :return: The result of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CheckCommon.

        The overall result of the check, based on the results of the constituent reports. Read-only.  # noqa: E501

        :param result: The result of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def download_uri(self):
        """Gets the download_uri of this CheckCommon.  # noqa: E501

        A link to a PDF output of the check results. Append `.pdf` to get the pdf file. Read-only.  # noqa: E501

        :return: The download_uri of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._download_uri

    @download_uri.setter
    def download_uri(self, download_uri):
        """Sets the download_uri of this CheckCommon.

        A link to a PDF output of the check results. Append `.pdf` to get the pdf file. Read-only.  # noqa: E501

        :param download_uri: The download_uri of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._download_uri = download_uri

    @property
    def form_uri(self):
        """Gets the form_uri of this CheckCommon.  # noqa: E501

        A link to the applicant form, if the check is of type `standard`. Read-only.  # noqa: E501

        :return: The form_uri of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._form_uri

    @form_uri.setter
    def form_uri(self, form_uri):
        """Sets the form_uri of this CheckCommon.

        A link to the applicant form, if the check is of type `standard`. Read-only.  # noqa: E501

        :param form_uri: The form_uri of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._form_uri = form_uri

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this CheckCommon.  # noqa: E501

        For `standard` checks, redirect to this URI when the applicant has submitted their data. Read-only.  # noqa: E501

        :return: The redirect_uri of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this CheckCommon.

        For `standard` checks, redirect to this URI when the applicant has submitted their data. Read-only.  # noqa: E501

        :param redirect_uri: The redirect_uri of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def results_uri(self):
        """Gets the results_uri of this CheckCommon.  # noqa: E501

        A link to the corresponding results page on the Onfido dashboard.  # noqa: E501

        :return: The results_uri of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._results_uri

    @results_uri.setter
    def results_uri(self, results_uri):
        """Sets the results_uri of this CheckCommon.

        A link to the corresponding results page on the Onfido dashboard.  # noqa: E501

        :param results_uri: The results_uri of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._results_uri = results_uri

    @property
    def type(self):
        """Gets the type of this CheckCommon.  # noqa: E501

        The type of the check, `standard` or `express`.  # noqa: E501

        :return: The type of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckCommon.

        The type of the check, `standard` or `express`.  # noqa: E501

        :param type: The type of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def report_type_groups(self):
        """Gets the report_type_groups of this CheckCommon.  # noqa: E501

        Array containing ids of the Report type groups being requested for. Write-only.  # noqa: E501

        :return: The report_type_groups of this CheckCommon.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_type_groups

    @report_type_groups.setter
    def report_type_groups(self, report_type_groups):
        """Sets the report_type_groups of this CheckCommon.

        Array containing ids of the Report type groups being requested for. Write-only.  # noqa: E501

        :param report_type_groups: The report_type_groups of this CheckCommon.  # noqa: E501
        :type: list[str]
        """

        self._report_type_groups = report_type_groups

    @property
    def tags(self):
        """Gets the tags of this CheckCommon.  # noqa: E501

        Array of tags being assigned to this check.  # noqa: E501

        :return: The tags of this CheckCommon.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CheckCommon.

        Array of tags being assigned to this check.  # noqa: E501

        :param tags: The tags of this CheckCommon.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def suppress_form_emails(self):
        """Gets the suppress_form_emails of this CheckCommon.  # noqa: E501

        For standard checks, applicant form will not be automatically sent if this is set to true. You can manually send the form at any time after the check has been created, using the link found in the form_uri attribute of the check object. Write-only.   # noqa: E501

        :return: The suppress_form_emails of this CheckCommon.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_form_emails

    @suppress_form_emails.setter
    def suppress_form_emails(self, suppress_form_emails):
        """Sets the suppress_form_emails of this CheckCommon.

        For standard checks, applicant form will not be automatically sent if this is set to true. You can manually send the form at any time after the check has been created, using the link found in the form_uri attribute of the check object. Write-only.   # noqa: E501

        :param suppress_form_emails: The suppress_form_emails of this CheckCommon.  # noqa: E501
        :type: bool
        """

        self._suppress_form_emails = suppress_form_emails

    @property
    def charge_applicant_for_check(self):
        """Gets the charge_applicant_for_check of this CheckCommon.  # noqa: E501

        For standard checks, applicants will be presented with a mandatory payment screen before they can submit the applicant form, if this is set to true. In this case, your account will not be charged. Write-only.   # noqa: E501

        :return: The charge_applicant_for_check of this CheckCommon.  # noqa: E501
        :rtype: bool
        """
        return self._charge_applicant_for_check

    @charge_applicant_for_check.setter
    def charge_applicant_for_check(self, charge_applicant_for_check):
        """Sets the charge_applicant_for_check of this CheckCommon.

        For standard checks, applicants will be presented with a mandatory payment screen before they can submit the applicant form, if this is set to true. In this case, your account will not be charged. Write-only.   # noqa: E501

        :param charge_applicant_for_check: The charge_applicant_for_check of this CheckCommon.  # noqa: E501
        :type: bool
        """

        self._charge_applicant_for_check = charge_applicant_for_check

    @property
    def brand_id(self):
        """Gets the brand_id of this CheckCommon.  # noqa: E501

        ID of the brand under which the check should be conducted. Write-only.  # noqa: E501

        :return: The brand_id of this CheckCommon.  # noqa: E501
        :rtype: str
        """
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        """Sets the brand_id of this CheckCommon.

        ID of the brand under which the check should be conducted. Write-only.  # noqa: E501

        :param brand_id: The brand_id of this CheckCommon.  # noqa: E501
        :type: str
        """

        self._brand_id = brand_id

    @property
    def async(self):
        """Gets the async of this CheckCommon.  # noqa: E501

        If this is set to true, we will queue checks for processing and return a response immediately. You can configure webhooks to notify you when the report is complete. Write-only.   # noqa: E501

        :return: The async of this CheckCommon.  # noqa: E501
        :rtype: bool
        """
        return self._async

    @async.setter
    def async(self, async):
        """Sets the async of this CheckCommon.

        If this is set to true, we will queue checks for processing and return a response immediately. You can configure webhooks to notify you when the report is complete. Write-only.   # noqa: E501

        :param async: The async of this CheckCommon.  # noqa: E501
        :type: bool
        """

        self._async = async

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CheckCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
