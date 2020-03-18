from django.db import models

# Create your models here.
class todos(models.Model):
	todo = models.CharField(max_length = 200)
	completed = models.BooleanField(default = False)

	def __str__(self):
		return self.todo + ' | ' + str(self.completed)