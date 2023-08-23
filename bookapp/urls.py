from django.contrib import admin
from django.urls import path
#from .views import book_list, book_create, book
from . views import BookCreate, BookList, BookDetail

urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetail.as_view()),

]