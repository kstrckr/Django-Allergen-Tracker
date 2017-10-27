from django.conf.urls import url

from . import views
app_name = 'allergens'
urlpatterns = [
    url(r'^$', views.AllergenList.as_view()),
    url(r'^(?P<allergen>\D+)/$', views.CommentList.as_view(), name='comments'),

]