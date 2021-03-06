from django.contrib.auth.models import User
from django.test import Client
from django.utils.timezone import localdate
from pytest import fixture
from rest_framework.authtoken.models import Token

from src.models import ToDoList


@fixture
def user(db):
    return User.objects.create_user(
        username='test', email='saidazimovaziza@gmail.com',
        password='test',
    )


@fixture
def authenticated_author_client(
        user, client: Client
) -> Client:
    token = Token.objects.get_or_create(user=user)[0].key
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {token}'
    print(client)
    return client


@fixture
def todo(db, user):
    return ToDoList.objects.create(
        user=user,
        title='Test task',
        description='Uchet kz test task',
        deadline=localdate(),
        executed=False
    )
