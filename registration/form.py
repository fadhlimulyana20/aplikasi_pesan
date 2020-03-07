from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta :
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nama Depan'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nama Belakang'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Konfirmasi Password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.field.help_text :
                 visible.field.widget.attrs.update({'class':'form-control has-popover', 'data-content':visible.field.help_text, 'data-placement':'bottom', 'data-container':'body'})

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     username_qs = User.objects.filter(username=username)

    # def is_space(string):
    #     if ' ' in string:
    #         return True
    #     return False

    #     if username_qs.exists():
    #         raise forms.ValidationError("Username sudah ada dan sudah dipakai orang lain")
    #         print("This Email is Already Used")
    #     elif not username.islower() and not is_space(username):
    #         raise forms.ValidationError("Username hanya boleh berisi huruf kecil dan angka.")
    #     elif is_space(username) and not username.islower():
    #         raise forms.ValidationError("Username tidak boleh mengandung spasi dan hanya boleh berisi huruf kecil dan angka.")
    #     elif is_space(username):
    #         raise forms.ValidationError("Username tidak boleh mengandung spasi dan hanya boleh berisi huruf kecil dan angka.")

    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("Alamat Email Sudah Dipakai")
    #         print("This Email is Already Used")
    #     return email
    
    # def clean_password2(self):
    #     password = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password != password2:
    #         raise forms.ValidationError("Password Harus sama")
    #     return password

class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=500 , widget=forms.Textarea, label="Tentang Anda", required=False)
    profession = forms.CharField(max_length=100, label="Profesi", required=False)
    institute = forms.CharField(max_length=100, label="Instansi", required=False)
    birth_date = forms.DateField(label="Tanggal Lahir", required=False)
    phone_number = forms.CharField(max_length=20, label="Nomor Telepon", required=False)
    image_profile = forms.ImageField(required=False, label="Foto Profil", widget=forms.FileInput)

    class Meta:
        model = Profile
        exclude = ['user', 'address']
        # widgets = {
        #     'birth_date': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'image_profile':
                visible.field.widget.attrs['class'] = 'form-control'
            # if visible.field.help_text :
            #      visible.field.widget.attrs.update({'class':'input100 has-popover', 'data-content':visible.field.help_text, 'data-placement':'bottom', 'data-container':'body'})

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'

    username.widget.attrs['placeholder'] = 'Username'
    password.widget.attrs['placeholder'] = 'Password'