"""codeandphilosophy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from registerStudent.views import ( 
	#AddStudentCreateView,
	AboutTemplateView,ContactTemplateView,
	RetrieveRegistrationTemplateView,
	ThanksTemplateView)

"""class based views are always CamelCased"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$',AboutTemplateView.as_view(), name ='about'),
    url(r'^contact/$',ContactTemplateView.as_view(), name ='contact'),
    url(r'^retrieve/$',RetrieveRegistrationTemplateView.as_view(), name = 'retrieve'),
    url(r'^thanks/$',ThanksTemplateView.as_view(), name = 'thanks-with-regnumber'),
    url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
    url(r'^$', include('registerStudent.urls', namespace='registerStudent')),
    #url(r'$',AddStudentCreateView.as_view(), name = 'add-student-create'),   
]

"""  url(r'$',AddStudentView.as_view()),  should be always at the end"""
