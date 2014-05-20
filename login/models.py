# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.core.validators import RegexValidator


username_validator = RegexValidator(
    re.compile('^[\w.@+-]+$'),
    'Enter a valid username.',
    'invalid'
)
