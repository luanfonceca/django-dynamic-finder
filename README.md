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
>>> Model.objects.get_by_name('Jonh')
# >>> Model.objects.get(name='Jonh')
<Model: #1 - Jonh>

>>> Model.objects.filter_by_name('Jonh')
# >>> Model.objects.filter(name='Jonh')
["<Model: #1 - Jonh>"]

>>> Model.objects.exclude_by_name('Jonh')
# >>> Model.objects.exclude(name='Jonh')
["<Model: #2 - Alice>", "<Model: #3 - Bob>"]

>>> Model.objects.filter_by_name_or_name('Jonh', 'Alice')
# >>> Model.objects.filter(Q(name='Jonh') | Q(name='Alice'))
["<Model: #1 - Jonh>", "<Model: #2 - Alice>"]

>>> Model.objects.exclude_by_name_or_id('Jonh', 3)
# >>> Model.objects.exclude(Q(name='Jonh') | Q(id=3))
["<Model: #2 - Alice>"]

>>> Model.objects.filter_by_name_or_id_or_name('Jonh', 3, 'Alice')
# >>> Model.objects.filter(Q(name='Jonh') | Q(id=3) | Q(name='Alice'))
["<Model: #1 - Jonh>", "<Model: #2 - Alice>", "<Model: #3 - Bob>"]
```
