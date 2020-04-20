
# Create your models here.
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=400)
	body = models.TextField()
	author = models.CharField(max_length=200)
	date = models.DateField(auto_now=True)

#str retourne self titre si j ai un objet article
	def __str__(self):
		return self.title


