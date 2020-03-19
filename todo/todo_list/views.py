from django.shortcuts import render, redirect
from .models import todos
from .forms import ToDoForm
from django.contrib import messages

# Create your views here.
def index(request):
	if request.method == "POST":
		form = ToDoForm(request.POST or None)
		
		if request.POST['todo'] == '':
			all_items = todos.objects.all
			messages.error(request, ('Invalid Todo !!'))
			return render(request, 'index.html', {'all_items' : all_items})
		elif form.is_valid():
			form.save()
			all_items = todos.objects.all
			messages.success(request, ('Todo has been added !!'))
			return render(request, 'index.html', {'all_items' : all_items})
	else:
		all_items = todos.objects.all
		return render(request, 'index.html', {'all_items' : all_items})

def delete(request, todo_id):
	todo = todos.objects.get(pk=todo_id)
	todo.delete()
	messages.success(request, ('Todo has been deleted !!'))
	return redirect('index')

def cross_off(request, todo_id):
	todo = todos.objects.get(pk=todo_id)
	todo.completed = True
	todo.save()
	return redirect('index')

def uncross(request, todo_id):
	todo = todos.objects.get(pk=todo_id)
	todo.completed = False
	todo.save()
	return redirect('index')

def edit(request, todo_id):
	if request.method == 'POST':
		todo = todos.objects.get(pk=todo_id)

		form = ToDoForm(request.POST or None, instance=todo)

		if form.is_valid():
			form.save()
			messages.success(request, ('Todo Has been changed successfully !!'))
			return redirect('index')

	else :
		todo = todos.objects.get(pk=todo_id)
		return render(request, 'edit.html', {'todo': todo})