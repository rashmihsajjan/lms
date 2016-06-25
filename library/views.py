from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Publisher, Author, Book, UserProfile, Issue
from library.forms import PublisherForm, AuthorForm, BookForm, UserProfileForm, IssueForm


def IndexView(request):
    return render(request, 'library/index.html', {})


def PublisherView(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'library/publisher.html', {'publisher_list': publisher_list})


def add_publisher(request):
    publisher_list = Publisher.objects.all()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            form = PublisherForm()
        return render(request, 'library/publisher.html', {'publisher_list': publisher_list, 'form':form})
    else:
        form = PublisherForm()
    return render(request, 'library/addpublisher.html', {'publisher_list': publisher_list, 'form':form})

def del_publisher(request,id):
    u = Publisher.objects.get(pk=id)
    u.delete()
    publisher_list = Publisher.objects.all()
    return render(request, 'library/publisher.html', {'publisher_list': publisher_list})

def edit_publisher(request, id):
    publisher_list = Publisher.objects.all()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            editform = form.save(commit=False)
            editform.name = request.name
            editform.save()

        return render(request, 'library/publisher.html', {'publisher_list': publisher_list, 'form':form})
    else:
        form = PublisherForm()
    return render(request, 'library/publisher.html', {'publisher_list': publisher_list, 'form':form})




    # if request.method == 'POST':
    #     form = PublisherForm(request.POST)
    #     if form.is_valid():
    #         form.u.delete()
    #         form.save()
    #         form = PublisherForm()

def AuthorView(request):
    author_list = Author.objects.all()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthorForm()
    else:
        form = AuthorForm()
    return render(request, 'library/author.html', {'author_list': author_list, 'form':form})


def BookView(request):
    book_list = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookForm()
    else:
        form = BookForm()
    return render(request, 'library/book.html', {'book_list': book_list, 'form':form})


def UserProfileView(request):
    userprofile_list = UserProfile.objects.all()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserProfileForm()
    else:
        form = UserProfileForm()
    return render(request, 'library/userprofile.html', {'userprofile_list': userprofile_list, 'form':form})


def IssueView(request):
    issue_list = Issue.objects.all()
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            form = IssueForm()
    else:
        form = IssueForm()
    return render(request, 'library/issue.html', {'issue_list': issue_list, 'form':form})
