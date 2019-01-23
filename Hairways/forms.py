from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Hairways.models import Users


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'phone', 'password', 'confirm_Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))


class ClientLoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
