from django.db import models

class teacher(models.Model):
	name = models.CharField(max_length=256)
	subject = models.CharField(max_length=256)
	teacher_photo = models.ImageField(upload_to='imageFiles', blank=True)
	uni_sub = models.CharField(max_length=250,null=True)
	uni = models.CharField(max_length=250,null=True)

	def __str__(self):
		return self.name