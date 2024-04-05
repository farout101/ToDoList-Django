from django.shortcuts import render, redirect
from django.http import HttpRequest
from . models import ToDoApp

# Create your views here.
def todoList(request):
    allData = {'todoList':ToDoApp.objects.all()}
    return render(request,'mainApp/todo_list.html',allData)

def insert_todo(request:HttpRequest):
    todo = ToDoApp(content = request.POST['content'])
    todo.save()
    return redirect('/todo/list/')

def delete_todo_item(request,todo_id):
    todoDelete =  ToDoApp.objects.get(id=todo_id)
    todoDelete.delete()
    return redirect('/todo/list/')