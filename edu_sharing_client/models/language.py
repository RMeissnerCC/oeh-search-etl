# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Language(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language': 'str',
        'string': 'list[KeyValuePair]'
    }

    attribute_map = {
        'language': 'language',
        'string': 'string'
    }

    def __init__(self, language=None, string=None):  # noqa: E501
        """Language - a model defined in Swagger"""  # noqa: E501
        self._language = None
        self._string = None
        self.discriminator = None
        if language is not None:
            self.language = language
        if string is not None:
            self.string = string

    @property
    def language(self):
        """Gets the language of this Language.  # noqa: E501


        :return: The language of this Language.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Language.


        :param language: The language of this Language.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def string(self):
        """Gets the string of this Language.  # noqa: E501


        :return: The string of this Language.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this Language.


        :param string: The string of this Language.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._string = string

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Language, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Language):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
