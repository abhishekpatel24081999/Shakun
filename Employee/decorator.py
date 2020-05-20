from django.core.exceptions import PermissionDenied
from Owner.models import Employee

from functools import wraps
from django.http import HttpResponseRedirect

def employee_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        obj = Employee.objects.filter(user = request.user)
        if obj != 0:
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
  return wrap