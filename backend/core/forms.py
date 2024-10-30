from django import forms
from .models import User  # Import your custom User model
from django import forms
from .models import Book, Folder
from allauth.account.forms import SignupForm, LoginForm, AddEmailForm
from django import forms



# class CustomEmailForm(AddEmailForm):
#     error_messages = {
#         'email_required': 'Please enter a valid email address.',
#     }

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise forms.ValidationError(self.error_messages['email_required'])
#         return email

class CustomSignupForm(SignupForm):
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password:
            errors = []
            if len(password) < 8:
                errors.append("Password must contain at least 8 characters.")
            if password.isdigit():
                errors.append("Password can't be entirely numeric.")
            if errors:
                raise forms.ValidationError(errors)
        return password

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


# class CustomLoginForm(LoginForm):
#     error_messages = {
#         'username_password_mismatch': 'The username and/or password you specified are not correct.'
#     }

#     def clean(self):
#         super().clean()
#         if self.errors:
#             raise forms.ValidationError(self.error_messages['username_password_mismatch'])
#         return self.cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'total_pages', 'comment', 'folder']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }
    
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'is_public']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Folder Name'}),
            'is_public': forms.CheckboxInput(attrs={'label': 'Share Publicly'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
        }
