"""
    ya empty right lets get busy.
    first we need the path function or method and then  the view we created inside the views.py file
    we can get them from the following import  from django and the view.py file.
"""

from django.urls import  path
from .views import home, about

"""we create a urlpattern which contain a list of path for our browser to interact with
so we have paht('/', function, name="") like what we have below and a "," to show we are the next line.
"""
urlpatterns =[
    path('', home, name="home"),
    path('about/', about, name="about"),
]

""" ones we create a urls by default django does not know how to connect to it so we have to link it to a project urls.py
so now you have to go to project urls.py"""