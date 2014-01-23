Django Dynamic Finder
=====================
A Django version of the Rails Dynamic Finder, using Django Managers.


# Install
```sh
$ pip install django-dynamic-finder
```

# Setup
```python
# settings.py

INSTALLED_APPS = (
    ...
    'django_dynamic_finder',
    ...
)
```

```python
# project/app/models.py

from django.db import models

from django_dynamic_finder.managers import DynamicFinderManager

class Model(models.Model):
    name = models.CharField(max_length=50)
    
    objects = DynamicFinderManager()
```
# Usage
```python
>>> Model.objects.get_by_name('Jonh') # Equivalent of Model.objects.get(name='Jonh')
<Model: #1 - Jonh>
>>> Model.objects.filter_by_name('Jonh') # Equivalent of Model.objects.filter(name='Jonh')
["<Model: #1 - Jonh>"]
>>> Model.objects.exclude_by_name('Jonh') # Equivalent of Model.objects.exclude(name='Jonh')
["<Model: #2 - Alice>", "<Model: #3 - Bob>"]
```
