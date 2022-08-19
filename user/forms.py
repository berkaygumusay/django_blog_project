from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length= 50 , label= "Username")
    password = forms.CharField(max_length= 20 , label= "Password" , widget= forms.PasswordInput)
    pwConfirm = forms.CharField(max_length= 20 , label= "Confirm Password" , widget= forms.PasswordInput)    
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        pwConfirm = self.cleaned_data.get("pwConfirm")

        if password and pwConfirm and password != pwConfirm : 
            raise forms.ValidationError("Passwords Are Not Same")
        values = {
            "username" : username,
            "password" : password
        }
        return values


class loginForm(forms.Form):
    username = forms.CharField(max_length= 50 , label= "Username")
    password = forms.CharField(max_length= 20, label="Password" , widget= forms.PasswordInput)