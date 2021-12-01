<<<<<<< HEAD
from django.contrib.auth.forms import AuthenticationForm
=======
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms, HiddenInput
>>>>>>> parent of bf133bd (Revert "04 django homework")

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of bf133bd (Revert "04 django homework")


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            'username',
            'first_name',
            'email',
            'age',
            'avatar',
            'password1',
<<<<<<< HEAD
            'password2'
=======
            'password2',
>>>>>>> parent of bf133bd (Revert "04 django homework")
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data_age = self.changed_data['age']
        if data_age < 18:
<<<<<<< HEAD
            raise forms.ValidationError('Вам мало лет.')
=======
            raise forms.ValidationError('Вам мало лет')
>>>>>>> parent of bf133bd (Revert "04 django homework")
        return data_age

    # def clean_email(self):
    #     data_email = self.changed_data['email']
    #     return data_email


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'avatar',
            'password',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = HiddenInput()

    # def clean_email(self):
    #     data_email = self.changed_data['email']
    #     return data_email

    def clean_age(self):
        data_age = self.changed_data['age']
        if data_age < 18:
            raise forms.ValidationError('Вам мало лет')
        return data_age
<<<<<<< HEAD
=======
>>>>>>> parent of b223c26 (complite)
=======
>>>>>>> parent of bf133bd (Revert "04 django homework")
