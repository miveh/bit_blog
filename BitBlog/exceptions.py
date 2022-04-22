from rest_framework import status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

msg = 'با این شناسه یافت نشد.'
_status_code = status.HTTP_404_NOT_FOUND


class PostDoesNotExistException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('پستی با این مشخصات وجود ندارد.')