# dtp.py
simple DTP (Desktop Publishing )tags for django content

To use:

1. paste dtp.py in templatetags folder in your Django project (if doesn't exist, create it - don’t forget the __init__.py file to ensure the directory is treated as a Python package [https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/]).

2. In template file write somewhere: {% load dtp %}

3. In place, you want to fix typography, just use it as common tag, ie:
  {{ section.content|removeOrphans }}
where section.content is your input, and __removeOrphans__ is filter name.
