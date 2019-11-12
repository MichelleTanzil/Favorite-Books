from django.db import models
from datetime import date, datetime
import re

# Create your models here.


class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        LETTER_REGEX = re.compile(r'^[a-zA-Z]*$')
        if not LETTER_REGEX.match(post_data['first_name']) or len(post_data['first_name']) < 2:
            errors['first_name'] = "The first name field is required and should be at least 2 characters long."
        if not LETTER_REGEX.match(post_data['last_name']) or len(post_data['last_name']) < 2:
            errors['last_name'] = "The last name field is required and should be at least 2 characters long."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = ("Invalid email address or email!")
        if User.objects.filter(email=post_data['email']).exists():
            errors['email'] = ("Email already exists, try logging in.")
        if len(post_data['password']) < 8 or len(post_data['password']) == 0:
            errors['password'] = "The password field is required and should be at least 8 characters long."
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Your passwords do not match, try again!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # liked_books = a list of books a given user likes
    # books_uploaded = a list of books uploaded by a given user

    def __repr__(self):
        return f"<User Object: {self.id} {self.first_name} {self.last_name}>"


class BookManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['title']) == 0:
            errors['title'] = "The title of the book is required, please enter it!"
        if len(post_data['desc']) < 5:
            errors['desc'] = "The description of the book must be at least 5 characters long."
        return errors


class Book(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    # the user who uploaded a given book
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    # a list of users who like a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __repr__(self):
        return f"<Book Object: {self.id} {self.title} {self.desc}>"
