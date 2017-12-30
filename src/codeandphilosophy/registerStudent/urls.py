from django.conf.urls import url

from .views import ( 
	AddStudentCreateView)

"""class based views are always CamelCased"""

urlpatterns = [
    url(r'',AddStudentCreateView.as_view(), name='add-student-create'), #don't include $ sign as this is already included in parent urls.py
] 