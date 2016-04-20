from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^users/tasks/(?P<token>[\w-]+)', views.UserTaskTokenView.as_view(), name='tasks_by_token'),
    url(r'^api-auth/tokenizer/', views.TokenView.as_view(), name='tokenizer'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
