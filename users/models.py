from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """User model."""
    username = PhoneNumberField(unique=True)
    email = models.EmailField(_('email address'), unique=True)
    code = models.IntegerField(null=True)
    invait_code = models.CharField(max_length=6, null=True)
    invait_code_user = models.CharField(max_length=6, null=True)

    def __str__(self):
        return str(self.username)

    # class Meta:
    #     managed = False
