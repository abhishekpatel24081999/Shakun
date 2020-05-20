from functools import wraps
from django.shortcuts import redirect
from .models import Profile,Location

def check_profile(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = Profile.objects.filter(user=request.user)
          
          obj = Location.objects.filter(user=request.user)
          location = set(val.city for val in obj)
          city = request.COOKIES["city"]

          if city in location:
               pass
          else:
               o = Location.objects.create(user=request.user,city=city)
               o.save()
                    
          if profile != 0:
               for data in profile:
                    if data.fname == "":
                         print("bye")
                         return redirect("/editprofile/")
                    else:
                         print("hii")
                         return function(request, *args, **kwargs)
          else:
               return function(request, *args, **kwargs)

     return wrap

def check_city(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          if "city" in request.COOKIES:
               return function(request, *args, **kwargs)
          else:
               return redirect("/")
     return wrap