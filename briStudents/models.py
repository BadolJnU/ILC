from django.db import models

class students(models.Model):
	name = models.CharField(max_length=256)
	subject = models.CharField(max_length=256)
	university = models.CharField(max_length=256)
	batch = models.IntegerField()
	student_photo = models.ImageField(upload_to='imageFiles', blank=True)
	

	def __str__(self):
		return self.name