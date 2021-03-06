from typing import Tuple
from django.utils.timezone import get_current_timezone
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    title = serializers.CharField(
        required=True,
    )
    description = serializers.CharField(
        required=True,
    )
    deadline = serializers.DateField(
        required=True,
    )
    executed = serializers.BooleanField(
        required=False,
    )

    class Meta:
        model = ToDoList
        fields: Tuple = (
            'user', 'title', 'description',
            'deadline', 'executed'
        )


class ToDoExecutedSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault(),
    # )
    executed = serializers.BooleanField(
        required=True,
    )

    class Meta:
        model = ToDoList
        fields: Tuple = (
            'executed',
        )