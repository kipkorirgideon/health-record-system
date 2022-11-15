from allauth.account.forms import LoginForm, SignupForm
import django.forms

from accounts.models import User

BLANK_CHOICE = (('', '---'),)
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = django.forms.TextInput(attrs={'placeholder': 'Email Address'})
        self.fields['login'].label = "Email Address"


class CustomSignupForm(SignupForm):
    first_name = django.forms.CharField(max_length=30, label='First Name', required=True)
    last_name = django.forms.CharField(max_length=30, label='Last Name', required=True)
    user_type = django.forms.ChoiceField(choices=BLANK_CHOICE + User.USER_TYPE_CHOICES, label='User Type', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = django.forms.TextInput(attrs={'placeholder': 'Email Address'})
        self.fields['email'].label = "Email Address"
        self.fields['password1'].widget = django.forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password1'].label = "Password"
        self.fields['password2'].widget = django.forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
        self.fields['password2'].label = "Confirm Password"

    field_order = (
        'first_name',
        'last_name',
        'email',
        'user_type',
        'password1',
        'password2',
        )
