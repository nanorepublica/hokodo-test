from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExerciseConfig(AppConfig):
    name = "reading_list_api.exercise"
    verbose_name = _("Exercise")
