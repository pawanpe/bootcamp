from django.core.exceptions import ValidationError
#from .models import StudentDetailsModel

def validate_even(value):
	''''''

def validate_name(value):
	''''''

def validate_location(value):
	''' clean_name is generally a method associated to a form. Where as validate_ is a general validation procedure.'''

def validate_registration(value):
	'''qs = StudentDetailsModel.objects.filter(registrationNumber__iexact=value)
	if qs.exists():
		raise ValidationError(f"Duplicate registraion Number. Try again!")
	return value'''
	'''raise ValidationError(f"Didnot find registration number {value}") # use it as raw string'''