from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.generic import View
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from .permissions import IsOwnerOrReadOnly
from .models import Task
from .serializers import TaskSerializer, UserSerializer, TokenSerializer, ErrorSerializer
from .forms import UserForm


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
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTaskTokenView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
                          
    def error_response_default(self, message, error=True):
        return { 'error': error, 'message': message }
        
    def get(self, request, token, format=None):
        try:
            user = User.objects.get(auth_token__key=token)
            userTasks = UserSerializer(user, context={'request':request})
            return Response(userTasks.data, status=status.HTTP_200_OK)
        except Exception as e:
            responseError = self.error_response_default(unicode(e))
            errorSerializer = ErrorSerializer(data=responseError)
            return Response(errorSerializer.initial_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


@permission_classes((permissions.AllowAny,))
class TokenView(APIView):
    '''
    Retrive Token. Only POST or GET
    '''
    def get_object(self, user):
        try:
            return Token.objects.get(user=user)
        except Token.DoesNotExist:
            return Http404
            
    def error_response_default(self, message, error=True):
        return { 'error': error, 'message': message }
        
    def post(self, request, format=None):
        try:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)
                    userSerializer =  UserSerializer(user, context={'request': request})
                    tokenSerializer = TokenSerializer(data={
                        'token': token.key,
                        'user': userSerializer.data
                    })
                    return Response(tokenSerializer.initial_data, status=status.HTTP_200_OK)
                else:
                    responseError = self.error_response_default(u'Usuario no esta activo')
                    errorSerializer = ErrorSerializer(data=responseError)
                    return Response(errorSerializer.initial_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                # the authentication system was unable to verify the username and password
                responseError = self.error_response_default(u'Usuario no existe')
                errorSerializer = ErrorSerializer(data=responseError)
                return Response(errorSerializer.initial_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            responseError = self.error_response_default(unicode(e))
            errorSerializer = ErrorSerializer(data=responseError)
            return Response(errorSerializer.initial_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'tasks': reverse('task-list', request=request, format=format)
    })


class UserFormView(View):
    form_class = UserForm
    template_name = 'form_user.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, { 'form': self.form_class })