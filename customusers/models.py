from django.contrib.auth.models import AbstractUser , UserManager , User
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext as _
import re
from .utils import BaseErrors
from .validators import PhoneValidator , UnicodeUsernameValidator , FirstNameValidator , CheckPasswords
from django.core.exceptions import ValidationError

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.username}-{ext}-{new_name}-{instance.is_whore}"
    return f"profile/{final_name}"


class UserManager(BaseUserManager):
    def create_user(self, phone_number=None, password=None , re_password=None):
        ph = re.search('^(\+98|0)?9\d{9}$', phone_number)
        if not ph:
            raise ValueError(BaseErrors.phone_number_regex)
        if password != re_password:
            raise ValidationError(BaseErrors.password_match)
        user = self.model(
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number=None, password=None):
        ph = re.search('^(\+98|0)?9\d{9}$' , phone_number)
        if not ph:
            raise ValueError(BaseErrors.phone_number_regex)
        else:
            print('asdf')
        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class CustomUsers(AbstractUser , models.Model):
    username_validator = UnicodeUsernameValidator()
    phone_validator = PhoneValidator()
    username = models.CharField(
        _("username"),
        max_length=200,
        help_text=_('200 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'max_length': _("length is not acceptable"),
        },
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        unique=True,
        validators=[phone_validator],
        help_text = _(
            "your phone number will be used to authenticate you next time +989121111111"
        ),
        error_messages={
            'unique': _("phone already exists."),
            'max_length':_('length is not acceptable ')
        },


    )
    first_name = models.CharField(
            _('first name'),
            max_length=150,
            blank=True,
            validators=[ FirstNameValidator ]
        )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True
    )
    is_vip = models.BooleanField(
        default = False ,
        verbose_name = _("is a vip")
    )
    date_updated = models.DateTimeField(
        auto_now = True,
        verbose_name = _("date updated")
    )
    profile_image = models.ImageField(
        upload_to=upload_image_path,
        blank = True ,
        null = True
    )
    password = models.CharField(
        _('password'),
        max_length=128,
    )
    re_password = models.CharField(
        max_length=128,
        blank=True,
    )
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
    def clean(self):
        if self.password != self.re_password:
            raise ValidationError("passwords don't match")
        # if "0" in self.phone_number[3]:
        #     raise ValidationError("0 not allowed")
    # def validate_unique(self, exclude=None):
    #     raise ValidationError("unique")
    def is_staff(self):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser



 #^(\+98|0)?9\d{9}$