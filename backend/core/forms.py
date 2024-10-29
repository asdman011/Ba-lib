from django import forms
from .models import User  # Import your custom User model
from django import forms
from .models import Book, Folder
from allauth.account.forms import SignupForm
from django import forms

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
