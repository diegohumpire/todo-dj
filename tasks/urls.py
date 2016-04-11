from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import TaskViewSet, UserViewSet, api_root
# import views

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

task_highlight = TaskViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^$', api_root),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task-list'),
    # url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task-detail'),
    # url(r'^tasks/(?P<pk>[0-9]+)/highlight/$', views.TaskHighLight.as_view(), name='task-title'),
    # url(r'^users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^tasks/$', task_list, name='task-list'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', task_detail, name='task-detail'),
    url(r'^tasks/(?P<pk>[0-9]+)/highlight/$', task_highlight, name='task-title'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
]

# Solo para DEV
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)