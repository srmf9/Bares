from django.conf.urls import include, url, patterns
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/bares/'
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^bares/', include('rango.urls')),
	url(r'^$', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
)