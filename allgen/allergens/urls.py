from django.conf.urls import url

from . import views
app_name = 'allergens'
urlpatterns = [
    url(r'^$', views.AllergenList.as_view(), name='root'),
    url(r'^(?P<allergen>\w+)/$', views.CommentList.as_view(), name='comments'),
    url(r'^(?P<allergen>\w+)/(?P<pk>\d+)/$', views.CommentDelete.as_view(), name='delete'),
    url(r'^(?P<allergen>\w+)/(?P<pk>\d+)/update/$', views.CommentUpdate.as_view(), name='update'),
    url(r'^(?P<allergen>\w+)/comment/$', views.CreateComment.as_view(), name='create-comment'),
]