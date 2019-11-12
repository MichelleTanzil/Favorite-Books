from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'main_app/index.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        if user:
            request.session['uid'] = user.id
        else:
            return redirect('/')
    return redirect('/books')


def login(request):
    user_list = User.objects.filter(email=request.POST['email'])
    if len(user_list) > 0:
        logged_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['uid'] = logged_user.id
            return redirect('/books')
    messages.error(request, "Invalid email and/or password")
    return redirect('/')


def books(request):
    if 'uid' not in request.session:
        messages.error(
            request, "You have not logged in or registered, please log in or register.")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['uid']),
        'all_books': Book.objects.all(),
        }
    return render(request, 'main_app/books.html', context)


def add_book(request, user_id):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(id=user_id)
        new_book = Book.objects.create(
            title=request.POST['title'], desc=request.POST['desc'], uploaded_by=user)
        new_book.users_who_like.add(user)
        return redirect('/books')


def book_profile(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
        'user': User.objects.get(id=request.session['uid'])
    }
    return render(request, 'main_app/book_profile.html', context)


def edit_book(request, book_id):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        book_in_question = Book.objects.get(id=book_id)
        book_in_question.title = request.POST['title']
        book_in_question.desc = request.POST['desc']
        book_in_question.save()
    return redirect(f'/books/{book_id}')


def delete_book(request, book_id):
    book_in_question = Book.objects.get(id=book_id)
    book_in_question.delete()
    return redirect(f'/books')


def unfavorite(request, book_id, user_id):
    book_in_question = Book.objects.get(id=book_id)
    unlike_user = User.objects.get(id=user_id)
    book_in_question.users_who_like.remove(unlike_user)
    return redirect(f'/books/{book_id}')


def add_to_favorites(request, book_id, user_id):
    book_in_question = Book.objects.get(id=book_id)
    like_user = User.objects.get(id=user_id)
    book_in_question.users_who_like.add(like_user)
    return redirect(f'/books/{book_id}')


def logout(request):
    request.session.clear()
    messages.error(request, "You have successfully logged out.")
    return redirect('/')


def favorite_books(request):
    context = {
      'user': User.objects.get(id=request.session['uid']),
    }
    return render(request, 'main_app/favorite_books.html', context)