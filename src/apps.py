from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SrcConfig(AppConfig):
    name = 'src'
    verbose_name = _('src')