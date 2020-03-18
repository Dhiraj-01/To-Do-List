from django import forms
from .models import todos

class ToDoForm(forms.ModelForm):
	class Meta:
		model = todos
		fields = ["todo", "completed"]