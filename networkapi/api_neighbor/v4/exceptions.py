# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.exceptions import APIException


class NeighborV4NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, msg):
        self.detail = u'NeighborV4 %s do not exist.' % (msg)


class NeighborV4Error(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, msg):
        self.detail = msg


class NeighborV6NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, msg):
        self.detail = u'NeighborV6 %s do not exist.' % (msg)


class NeighborV6Error(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, msg):
        self.detail = msg

