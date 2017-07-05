from django.conf.urls import patterns, url

urlpatterns = patterns(
	'api.views',
	url(r'^events/', 'event_post', name='event_post'),
	url(r'^event/get/(?P<UserDevice>\w{0,50})/$', 'event_detail', name='event_detail'),
	
	url(r'^adduser/', 'adduser', name='adduser'),

	url(r'^event/block/add/(?P<EventName>\w{0,50})/$', 'block_event_add', name='block_event_add'),
	url(r'^event/block/delete/(?P<EventName>\w{0,50})/$', 'block_event_delete', name='block_event_delete'),

)
