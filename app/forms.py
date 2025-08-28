from django import forms 
from .models import Student

# Model Form 
class StudentForm(forms.ModelForm):
    class Meta: 
        model = Student
        fields = "__all__"
        # fields = ['first_name', "last_name", "address", "email", "phone"]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': ' input w-full'}),
            'last_name' : forms.TextInput(attrs={'class': ' input w-full'}),
            'address' : forms.TextInput(attrs={'class': ' input w-full'}),
            'email' : forms.EmailInput(attrs={'class': ' input w-full'}),
            'phone' : forms.TextInput(attrs={'class': ' input w-full'}),
        }

    def clean_phone(self): 
        phone = self.cleaned_data['phone']

        try: 
            int(phone)  # 98adsklfh => Not possible to convert to int
        except ValueError:
            raise forms.ValidationError("Phone number must be numberic.")
        
        # Check firs two digits of phone is valid or not
        if phone[:2] not in ['98', '97']:
            raise forms.ValidationError("Phone number must start with 98 or 97")

        return phone 

# General Form
class StudentRegisterForm(forms.Form): 
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10, min_length=10)

    def clean_phone(self): 
        phone = self.cleaned_data['phone']

        try: 
            int(phone)  # 98adsklfh => Not possible to convert to int
        except ValueError:
            raise forms.ValidationError("Phone number must be numberic.")
        
        # Check firs two digits of phone is valid or not
        if phone[:2] not in ['98', '97']:
            raise forms.ValidationError("Phone number must start with 98 or 97")

        return phone 
    