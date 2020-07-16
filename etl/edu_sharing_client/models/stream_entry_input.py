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


class StreamEntryInput(object):
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
        'id': 'str',
        'title': 'str',
        'description': 'str',
        'nodes': 'list[str]',
        'properties': 'dict(str, object)',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'nodes': 'nodes',
        'properties': 'properties',
        'priority': 'priority'
    }

    def __init__(self, id=None, title=None, description=None, nodes=None, properties=None, priority=None):  # noqa: E501
        """StreamEntryInput - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._description = None
        self._nodes = None
        self._properties = None
        self._priority = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if nodes is not None:
            self.nodes = nodes
        if properties is not None:
            self.properties = properties
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        """Gets the id of this StreamEntryInput.  # noqa: E501


        :return: The id of this StreamEntryInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StreamEntryInput.


        :param id: The id of this StreamEntryInput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this StreamEntryInput.  # noqa: E501


        :return: The title of this StreamEntryInput.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StreamEntryInput.


        :param title: The title of this StreamEntryInput.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this StreamEntryInput.  # noqa: E501


        :return: The description of this StreamEntryInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StreamEntryInput.


        :param description: The description of this StreamEntryInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def nodes(self):
        """Gets the nodes of this StreamEntryInput.  # noqa: E501


        :return: The nodes of this StreamEntryInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this StreamEntryInput.


        :param nodes: The nodes of this StreamEntryInput.  # noqa: E501
        :type: list[str]
        """

        self._nodes = nodes

    @property
    def properties(self):
        """Gets the properties of this StreamEntryInput.  # noqa: E501


        :return: The properties of this StreamEntryInput.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this StreamEntryInput.


        :param properties: The properties of this StreamEntryInput.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def priority(self):
        """Gets the priority of this StreamEntryInput.  # noqa: E501


        :return: The priority of this StreamEntryInput.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this StreamEntryInput.


        :param priority: The priority of this StreamEntryInput.  # noqa: E501
        :type: int
        """

        self._priority = priority

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
        if issubclass(StreamEntryInput, dict):
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
        if not isinstance(other, StreamEntryInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other