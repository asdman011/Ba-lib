from django import forms
from .models import User  # Import your custom User model
from django import forms
from .models import Folder, Book

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'is_public']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Folder Name'}),
            'is_public': forms.CheckboxInput(attrs={'label': 'Share Publicly'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'current_page', 'published_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
        }
