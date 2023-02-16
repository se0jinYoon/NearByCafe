from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users


class SignupForm(UserCreationForm):
    class Meta():
        model = Users
        fields = ['username', 'email_address',
                  'password1', 'password2', 'realname']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username']
        self.fields['email_address'].widget.attrs.update(
            {'placeholder': 'example@example.com'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': '8자 이상 15자 이하의 영문,숫자만 가능'})
        self.fields['password2'].widget.attrs.update()
        self.fields['realname'].widget.attrs.update()
