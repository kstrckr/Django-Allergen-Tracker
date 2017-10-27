from django.conf.urls import url

from . import views
app_name = 'allergens'
urlpatterns = [
    url(r'^$', views.allergen_list.as_view()),
    url(r'^(?P<allergen>\D+)/$', views.DetailView.as_view(), name='comments'),

]