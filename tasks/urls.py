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
    url(r'^api-auth/tokenizer/', views.TokenView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
