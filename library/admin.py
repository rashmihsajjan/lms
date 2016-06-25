from django.contrib import admin
from .models import Publisher, Author, Book, UserProfile, Issue

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'country', 'website')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'isbn', 'publisher', 'publication_date', 'available')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'user_type', 'expiry_date')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'user_profile', 'issued_date', 'due_date', 'issued_by')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Issue, IssueAdmin)
