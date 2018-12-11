
'''from django import forms

class Name(forms.Form):

    first_name = forms.CharField( max_length=100)
    last_name = forms.CharField( max_length=100)'''



from allauth.account.forms import LoginForm
from django import forms


class YourLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(YourLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['login'].widget.attrs['placeholder'] = "Email"

        # You don't want the `remember` field?
        if 'remember' in self.fields.keys():
            del self.fields['remember']
