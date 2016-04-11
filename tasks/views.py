from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#
# class TaskHighLight(generics.GenericAPIView):
#     queryset = Task.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         task = self.get_object()
#         return Response('{} - {}'.format(task.title, task.description))


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        task = self.get_object()
        return Response('{} - {}'.format(task.title, task.description))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })