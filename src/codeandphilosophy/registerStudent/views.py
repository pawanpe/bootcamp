import random
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, CreateView
from django.views.generic import TemplateView

from registerStudent.models import StudentDetailsModel
from registerStudent.forms import StudentDetailsForm
# Create your views here.

class AddStudentCreateView(CreateView):
	template_name = 'baseform.html' #template_name, form_class and success_url are django related variables
	form_class = StudentDetailsForm
	#model = StudentDetailsModel
	#fields = ('name', 'location', 'email','registrationNumber')
	#context_object_name
	#
	'''def get_object(self):	
		object = super(AddStudentCreateView,self).get_object()
		object['registrationNumber'] = random.randint(1, 9999999)
		object.save()
		print("Printing object now *******" + object)
		return object'''


	#def get_context_data(self, *args, **kwargs):
	#	context = super(ContactTemplateView,self).get_context_data(*args, **kwargs)

	#success_url = '/thanks/' #  defined with get_absolute_url in model

	'''If you use AddStudentFormView(FormView)
		def form_valid(self,form):		
		# This method is called when valid form data has been POSTed.
		
		if self.request.method == 'POST':
			#name = self.request.POST["name"] # OR self.request.POST.get("title")
			#location = self.request.POST["location"]
			#email = self.request.POST["email"]
			#StudentDetailsModel.objects.create(
		#		name = name,
		#		location = location,
		#		email = email
		#		)
			form = StudentDetailsForm(self.request.POST)
			if form.is_valid(): # For avoiding 'StudentDetailsForm' object has no attribute 'cleaned_data' -- Attribure Error
				StudentDetailsModel.objects.create(
					name = form.cleaned_data.get('name'),
					location = form.cleaned_data.get('location'),
					email = form.cleaned_data.get('email')
					)

			if form.errors:
				print(form.errors)

		form.send_email_on_success()
		#return super().form_valid(form) --> This is in Django 2.0
		return super(AddStudentFormView,self).form_valid(form)'''
	
class ThanksTemplateView(TemplateView):
	template_name = 'thanks.html'

class ContactTemplateView(TemplateView):
	template_name = 'contact.html'
	"""By default template view methods will give default implementation of other methods such 
	as get_context_data(). Use something like below to override those functions customizing them

	def get_context_data(self, *args, **kwargs):
		context = super(ContactTemplateView,self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self,*args,**kwargs)"""
	

class AboutTemplateView(TemplateView):
	template_name = 'about.html'
	#

class RetrieveRegistrationTemplateView(TemplateView):
	
	""" def get_queryset(self):
			print(self.kwargs)
			qs = StudentDetailsModel.objects.filter(name__iexact='' && email__iexact='')
			StudentDetailsModel.objects.get(id=RegNumberVariable) --> check DetailView for this immplementation
			return qs"""
	template_name = 'retrieve.html'