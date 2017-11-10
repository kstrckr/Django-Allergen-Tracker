from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # global admin URL
    url(r'^admin/', admin.site.urls),
    # incudes all allergen URLs
    url(r'^', include('allergens.urls')),
]
