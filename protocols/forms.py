from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class JoinForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()
    profile = forms.CharField()
    email = forms.CharField()

class ProtocolForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()


class TagForm(forms.Form):
    tag = forms.CharField()

class CommentForm(forms.Form):
    comment = forms.CharField()
