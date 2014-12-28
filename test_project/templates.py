from django.template.base import TemplateDoesNotExist
from django.template.loader import BaseLoader


class TestLoader(BaseLoader):
    is_usable = True

    def load_template_source(self, template_name, template_dirs=None):
        if template_name == '404.html':
            return ('404 error', None)
        else:
            raise TemplateDoesNotExist(template_name)
