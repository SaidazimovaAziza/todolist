from typing import Tuple

import django
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from src.models import ToDoList
from src.serializers import ToDoSerializer, ToDoExecutedSerializer
from src.helpers import send_mail_to_user
from django.contrib.auth import urls



class ToDoViewSet(ModelViewSet):
    authentication_classes: Tuple = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication
    )
    http_method_names = ('post', 'get', 'patch', 'delete')
    serializer_class = ToDoSerializer
    queryset = ToDoList.objects.order_by('-id')
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=('post',))
    def execute(self, request, pk):
        todo = ToDoList.objects.get(pk=pk)
        serializer = ToDoExecutedSerializer(
            instance=todo,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            send_mail_to_user.apply(kwargs={
                'user': todo.user.email,
                'title': todo.title,
                'executed': todo.executed
            })
        return Response(serializer.data)



