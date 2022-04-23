from rest_framework import status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class CreateRateException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('oppss! please try again')
