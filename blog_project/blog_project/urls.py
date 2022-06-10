"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
""" now we have to  import include along with path as we have below """
from django.urls import path, include



""" we have to include the file and this will tell django where to look from to get the part in our in this case blog app as we have below."""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls'))
]


"""
  ok  am going to be repeating this process try looking at the cold to see a pattern. Now go back to you urls.py in your blogapp to creatw another view
"""