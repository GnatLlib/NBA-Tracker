from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,

    )
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': ' Passd'}))

    @property
    def clean(self):

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username = username, password=password)

        if not user:
            raise forms.ValidationError("Incorrect Login Info")

        if not user.is_active:
            raise forms.ValidationError("This user is not valid")

        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': ' Email Address'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': ' Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]





