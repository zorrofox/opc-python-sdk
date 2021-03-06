# coding: utf-8

"""
    Authenticate

    A POST request to this resource authenticates the specified user and returns an authentication cookie, which you can specify in subsequent API calls to Oracle Compute Cloud Service.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Authenticate(object):
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
        'password': 'str',
        'user': 'str'
    }

    attribute_map = {
        'password': 'password',
        'user': 'user'
    }

    def __init__(self, password=None, user=None):
        """
        Authenticate - a model defined in Swagger
        """

        self._password = None
        self._user = None

        self.password = password
        self.user = user

    @property
    def password(self):
        """
        Gets the password of this Authenticate.
        The password for the user.

        :return: The password of this Authenticate.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this Authenticate.
        The password for the user.

        :param password: The password of this Authenticate.
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def user(self):
        """
        Gets the user of this Authenticate.
        Two-part name of the user in the format, <code>/Compute-<em>identity_domain</em>/<em>user</em></code> (example: <code>/Compute-acme/joe.jonathan@example.com</code>)

        :return: The user of this Authenticate.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Authenticate.
        Two-part name of the user in the format, <code>/Compute-<em>identity_domain</em>/<em>user</em></code> (example: <code>/Compute-acme/joe.jonathan@example.com</code>)

        :param user: The user of this Authenticate.
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

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
        if not isinstance(other, Authenticate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
