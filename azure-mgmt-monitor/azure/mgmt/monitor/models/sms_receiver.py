# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SmsReceiver(Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The name of the SMS receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param country_code: The country code of the SMS receiver.
    :type country_code: str
    :param phone_number: The phone number of the SMS receiver.
    :type phone_number: str
    :ivar status: Possible values include: 'NotSpecified', 'Enabled',
     'Disabled'
    :vartype status: str or :class:`ReceiverStatus
     <azure.mgmt.monitor.models.ReceiverStatus>`
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ReceiverStatus'},
    }

    def __init__(self, name, country_code, phone_number):
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None
