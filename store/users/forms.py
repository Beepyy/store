from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].label="Логин"
        self.fields['password1'].label = 'Пароль 1'
        self.fields['password2'].label = 'Пароль 2'
        
        self.fields["username"].help_text="Введите свой будующий логин"
        self.fields['password1'].help_text = '8 символом,включая цифры'
        self.fields['password2'].help_text = 'Должены быть одинаковыми'
    class Meta:
        model = User
        fields = ["username", "password1","password2"]
