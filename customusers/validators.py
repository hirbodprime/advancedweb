from django.core import validators
from django.utils.translation import gettext as _
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r'^(\+98|0)?9\d{9}$'
    message = _("please enter the correct value +989121111111")
    flags = 0




@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0

def CheckPasswords(password , re_password):
    if password != re_password:
        raise ValidationError("passwords do not match")

def FirstNameValidator(first_name):
    if " " in first_name:
        raise ValidationError(f"please remove space from {first_name}")