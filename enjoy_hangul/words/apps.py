from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WordsConfig(AppConfig):
    name = "enjoy_hangul.words"
    verbose_name = _("Words")

    def ready(self):
        try:
            import enjoy_hangul.words.signals  # noqa F401
        except ImportError:
            pass
