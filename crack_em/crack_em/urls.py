from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from crack_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crack_em/', include('crack_app.urls')),
    url(r'^$', views.home, name= 'home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', views.MyRegistrationView.as_view(),
        name='registration_register'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    
    
    
    
    
    
    
    
    
    
    
    
    