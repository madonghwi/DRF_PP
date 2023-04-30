from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=1)
    introduction = forms.CharField(widget=forms.Textarea())
    gender = forms.ChoiceField(choices=[('male', '남자'), ('female', '여자'), ('other', '기타')])

    # 비밀번호 검증을 위한 clean 메서드 정의
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError(
                "비밀번호와 비밀번호 확인 값이 일치하지 않습니다."
            )
        return cleaned_data

class SigninForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ModifyForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), required=False)
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}), required=False)
    introduction = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Introduction'}), required=False)
