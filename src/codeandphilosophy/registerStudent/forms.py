from django import forms
from .models import StudentDetailsModel

'''class StudentDetailsForm(forms.Form):
	name = forms.CharField(required=True)
	location = forms.CharField(required=True)
	email =forms.EmailField(required=True)

	

	# TODO: write success implementation here.
	def send_email_on_success(self): # or send_email(self)
		pass'''


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetailsModel
        fields = ('name',
        	'location',
        	'email'
        )

    ''' Use this to reject obsene names
    	def clean_name(self):
     	name = self.cleaned_data.get('name')
     	if name == "Hello":
     	 	raise forms.ValidationError("Not a valid name")

     	return name 


     	def clean_location(self):
     	def clean_email(self):

     	'''
    