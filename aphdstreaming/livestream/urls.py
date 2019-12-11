from django.conf.urls import url

from . import views

app_name = 'livestream'

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Index,
        name='index'
    ),

    url(
        regex=r'^event/(?P<id>[0-9]+)/',
        view=views.Event_Stream,
        name='Event'
    ),

    url(
    	regex=r'^liveevent/add/$',
    	view =views.Event_Add,
    	name='Live_Event_Add'
    ),

]
