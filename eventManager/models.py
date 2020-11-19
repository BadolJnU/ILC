from django.db import models
from PIL import Image

class event(models.Model):
	title = models.CharField(max_length=1200, blank=False)
	date = models.DateField(blank=False)
	location = models.CharField(max_length=1200)
	short_description = models.TextField()
	title_image = models.ImageField(upload_to='imageFiles', blank=True)

	def __str__(self):
		return self.title