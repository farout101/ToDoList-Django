from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.todoList,name="todoList"),
    path('insert_todo/',views.insert_todo,name="insert_todo"),
    path('delete/<int:todo_id>/',views.delete_todo_item,name="delete_todo_item"),
]