#!/usr/bin/env python
# encoding: utf-8

"""
django_dynamic_finder/managers.py

Created by Luan Fonseca <luanfonceca@gmail.com> on 2014-01-23
"""

from django.db.models import manager, Q
from operator import or_

def create_Q_queries(fields, values):
    def make_Q(x):
        return Q(**{fields[x]: values[x]})
    return map(make_Q, range(len(values)))
    
class DynamicFinderManager(manager.Manager):
    def __getattr__(self, name):
        try:
            return super(DynamicFinderManager, self).__getattr__(self, name)
        except AttributeError:
            def _missing_manager(*args):
                if '_or_' in name:
                    method, fields = name.split('_by_')
                    missing_method = getattr(self, method)
                    fields = fields.split('_or_')
                    q_objs = create_Q_queries(fields, args)
                    return missing_method(reduce(or_, q_objs))
                elif '_by_' in name:
                    method, field = name.split('_by_')
                    missing_method = getattr(self, method)
                    return missing_method(**{field: args[0]})
            return _missing_manager

