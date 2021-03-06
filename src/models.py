from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class ToDoList(models.Model):
    user = models.OneToOneField(
        get_user_model(), verbose_name='Пользователь',
        on_delete=models.SET_NULL, null=True, related_name='todolist',
    )
    title = models.CharField(
        help_text=_('title'), verbose_name=_('title'),
        max_length=512, blank=True,
    )
    description = models.TextField(
        help_text=_('description'), verbose_name=_('description'),
        max_length=512, blank=True,
    )
    deadline = models.DateField(
        help_text=_('deadline'),
        verbose_name=_('deadline'),
    )
    executed = models.BooleanField(
        help_text=_('executed'),
        verbose_name=_('executed'),
        default=False
    )

    class Meta:
        verbose_name = _('todolist')
        verbose_name_plural = _('todolist')
