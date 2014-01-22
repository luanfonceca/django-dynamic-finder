#!/usr/bin/env python
# encoding: utf-8

"""
django_dynamic_finder/managers.py

Created by Luan Fonseca <luanfonceca@gmail.com> on 2014-01-23
"""

from django.db.models import manager

class DynamicFinderManager(manager.Manager):
    def __getattr__(self, name):
        try:
            return super(DynamicFinderManager, self).__getattr__(self, name)
        except AttributeError:
            def _missing_manager(value):
                method, field = name.split('_by_')
                missing_method = getattr(self, method)
                return missing_method(**{field: value})
            return _missing_manager

