from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

<<<<<<< HEAD
class Contact(
	TimeStampedModel, 
=======
class Locations(
	TimeStampedModel,
>>>>>>> 839b109450c436fd4bf894c62ca409bd4089be3d
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):

	class Meta:
		verbose_name_plural = "Locations"

	email = models.EmailField(verbose_name="Email")

	def __str__(self):
		return f'{self.title}'