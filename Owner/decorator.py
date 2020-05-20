from django.core.exceptions import PermissionDenied
from .models import Owner

from functools import wraps
from django.http import HttpResponseRedirect

def owner_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        obj = Owner.objects.filter(user = request.user)
        if obj != 0:
             return function(request, *args, **kwargs)
        else:
            # return HttpResponseRedirect('/')
            raise PermissionDenied
  return wrap