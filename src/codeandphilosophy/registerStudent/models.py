import random
from django.core.urlresolvers import reverse
from django.db import models
from django.urls import reverse
from .validators import (
	validate_registration,
	#validate_name,
	#validate_location
	)

# Create your models here.
class StudentDetailsModel(models.Model):
	name = models.CharField(max_length=256,null=False,blank=False, verbose_name='Your name according to ID')
	location = models.CharField(max_length=256, null=False,blank=False)
	email =models.EmailField(max_length=256,blank=False,null=False, verbose_name= 'Valid email please!')
	registrationNumber = models.IntegerField(blank=False, null=False,default=random.randint(1, 9999999),
		unique=True, validators=[validate_registration])
	datetime = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

	def get_absolute_url(self): #will override the default method for success_url in createView
		return reverse('thanks-with-regnumber') #, kwargs={'slug': self.slug})


	'''class Meta:
		ordering = ['-updated','-timestamp'] #-updated: recently added item at front'''