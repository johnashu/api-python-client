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


class WebhooksList(object):
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
        'webhooks': 'list[Webhook]'
    }

    attribute_map = {
        'webhooks': 'webhooks'
    }

    def __init__(self, webhooks=None):  # noqa: E501
        """WebhooksList - a model defined in OpenAPI"""  # noqa: E501

        self._webhooks = None
        self.discriminator = None

        if webhooks is not None:
            self.webhooks = webhooks

    @property
    def webhooks(self):
        """Gets the webhooks of this WebhooksList.  # noqa: E501


        :return: The webhooks of this WebhooksList.  # noqa: E501
        :rtype: list[Webhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this WebhooksList.


        :param webhooks: The webhooks of this WebhooksList.  # noqa: E501
        :type: list[Webhook]
        """

        self._webhooks = webhooks

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
        if not isinstance(other, WebhooksList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
