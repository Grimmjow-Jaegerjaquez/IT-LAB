"""
Definition of models.
"""

from pyexpat import model
from django.db import models
# Create your models here.

class RegisteredUser(models.Model):
	user_name = models.CharField(max_length=256, unique=True)
	password = models.CharField(max_length=128)
	email = models.EmailField(blank = True, null = True)
	phone_number = models.CharField(max_length=15, blank=True)

	def __str__(self):
		return self.user_name
