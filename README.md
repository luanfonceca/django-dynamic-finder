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
# Usage
```python
>>> Model.objects.get_by_name('Jonh') # Equivalent of Model.objects.get(name='Jonh')
<Model: #1 - Jonh>
>>> Model.objects.filter_by_name('Jonh') # Equivalent of Model.objects.filter(name='Jonh')
["<Model: #1 - Jonh>"]
>>> Model.objects.exclude_by_name('Jonh') # Equivalent of Model.objects.exclude(name='Jonh')
["<Model: #2 - Alice>", "<Model: #3 - Bob>"]
```
