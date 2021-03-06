from django.utils.timezone import localdate

from src.models import ToDoList
from django.test import Client


def test_login_and_logout(
        db, user, todo, client: Client
):
    client.login(username='test', password='test')
    response = client.patch(
        path=f'/api/todo/{todo.pk}/',
        data={
            'title': 'changed text',
        },
        content_type='application/json'
    )
    assert response.status_code == 200
    client.logout()
    response = client.patch(
        path=f'/api/todo/{todo.pk}/',
        data={
            'title': 'changed text',
        },
        content_type='application/json'
    )
    assert response.status_code == 401


def test_create_201(
        db, user, authenticated_author_client
) -> None:
    response = authenticated_author_client.post(
        path='/api/todo/',
        data={
            'title': 'Test task',
            'description': 'Uchet kz test task',
            'deadline': localdate(),
            'executed': False
        },
        content_type='application/json'
    )
    assert response.status_code == 201


def test_get_200(
        db, user, authenticated_author_client, todo
) -> None:
    response = authenticated_author_client.get(
        path='/api/todo/',
    )
    assert response.status_code == 200
    assert response.json() == [{
        'deadline': str(localdate()),
        'description': 'Uchet kz test task',
        'executed': False,
        'title': 'Test task'
    }]


def test_delete_203(
        db, user, authenticated_author_client, todo
) -> None:
    response = authenticated_author_client.delete(
        path=f'/api/todo/{todo.pk}/',
        content_type='application/json'
    )
    assert response.status_code == 204


def test_patch_200(
        db, user, authenticated_author_client, todo
):
    response = authenticated_author_client.patch(
        path=f'/api/todo/{todo.pk}/',
        data={
            'title': 'changed text',
        },
        content_type='application/json'
    )
    todo = ToDoList.objects.last()
    assert response.status_code == 200
    assert todo.title == 'changed text'


def test_post_200_executed(
        db, user, authenticated_author_client, todo
):
    response = authenticated_author_client.post(
        path=f'/api/todo/{todo.pk}/execute/',
        data={
            'executed': True,
        },
        content_type='application/json'
    )
    assert response.status_code == 200
    assert response.json() == {'executed': True}
