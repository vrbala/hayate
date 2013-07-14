# Helpers and other utils
import random

from django.http import HttpResponse
from django.forms.widgets import Input

class HttpTextResponse:

    def __init__(self, text, status):
        return HttpResponse(text, status = status, content_type = "text/plain")

class EmailInput(Input):
    input_type = 'email'

    def __init__(self, attrs):
        if attrs is not None:
            self.input_type = attrs.pop('type', self.input_type)
        super(EmailInput, self).__init__(attrs)

def randomString(length):
    x = ''
    for _ in range(length+1):
        x = x + str(random.randint(0, 9))