from django.template.base import TemplateDoesNotExist
try:
    # Django >= 1.8
    # https://docs.djangoproject.com/en/1.8/releases/1.8/#django-template-loader-baseloader
    from django.template.loaders.base import Loader as BaseLoader
except:
    from django.template.loader import BaseLoader


class TestLoader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        if template_name == '404.html':
            return ('404 error', None)
        else:
            raise TemplateDoesNotExist(template_name)
