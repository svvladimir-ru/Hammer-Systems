from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
# from phone_field import PhoneField
from .service import id_generator
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()


class CreationForm(forms.ModelForm):
    username = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Пример: +79671234455'}),
                                label="Номер телефона", required=False
                                )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)


class LoginForm(forms.Form):
    username = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Пример: +79671234455'}),
                                label="Номер телефона", required=False
                                )


class LoginCodeForm(forms.Form):
    code = forms.IntegerField()


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
