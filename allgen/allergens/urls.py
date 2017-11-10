from django.conf.urls import url

from . import views
app_name = 'allergens'
urlpatterns = [
    # base index url
    url(r'^$', views.AllergenList.as_view(), name='root'),
    # list all comments for specific allergen
    url(r'^(?P<allergen>\w+)/$', views.CommentList.as_view(), name='comments'),
    # comment delete URL
    url(r'^(?P<allergen>\w+)/(?P<pk>\d+)/$', views.CommentDelete.as_view(), name='delete'),
    # comment update URL
    url(r'^(?P<allergen>\w+)/(?P<pk>\d+)/update/$', views.CommentUpdate.as_view(), name='update'),
    # comment creation URL
    url(r'^(?P<allergen>\w+)/comment/$', views.CreateComment.as_view(), name='create-comment'),
]