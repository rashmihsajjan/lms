from django import forms
from library.models import Publisher, Author, Book, UserProfile, Issue


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state', 'country', 'website')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'email')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'price', 'isbn', 'authors', 'publisher', 'publication_date', 'available')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'address', 'user_type', 'expiry_date')

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('book', 'user_profile', 'issued_date', 'due_date', 'issued_by')