from django.conf.urls import url, include
from rest_framework import routers
from viewsets import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns_api = router.urls

urlpatterns = [
    url(r'^', include(urlpatterns_api))
]
