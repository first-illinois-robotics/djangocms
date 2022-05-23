from django import template
from django.template.defaultfilters import stringfilter
from urllib.parse import urlparse

register = template.Library()


@register.filter
@stringfilter
def is_external(value: str):
    parsed_url = urlparse(value)
    return parsed_url.netloc != ''
