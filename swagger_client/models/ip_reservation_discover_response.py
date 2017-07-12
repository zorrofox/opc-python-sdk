# coding: utf-8

"""
    IPReservations

    An IP reservation is the allocation of a public IP address from an IP address pool. After creating an IP reservation, you can associate it with an instance by using an IP association, to enable access between the Internet and the instance.<p>You can add, delete, update, and view IP reservations using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IPReservationDiscoverResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'result': 'list[str]'
    }

    attribute_map = {
        'result': 'result'
    }

    def __init__(self, result=None):
        """
        IPReservationDiscoverResponse - a model defined in Swagger
        """

        self._result = None

        if result is not None:
          self.result = result

    @property
    def result(self):
        """
        Gets the result of this IPReservationDiscoverResponse.

        :return: The result of this IPReservationDiscoverResponse.
        :rtype: list[str]
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this IPReservationDiscoverResponse.

        :param result: The result of this IPReservationDiscoverResponse.
        :type: list[str]
        """

        self._result = result

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IPReservationDiscoverResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
