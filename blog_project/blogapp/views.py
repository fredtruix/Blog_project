from django.shortcuts import render, HttpResponse
# Create your views here.


"""
    writing a django app could be scary some times expectually because of the many  folders and other files we see when
    we first create our project and even with are first app.
    but i promise you everything will start to make sense when we continue with this tutorial.

    remember we have to create a app at the begining of this project we run a python command on the terminal 
    "python manage.py startapp (and we added the app name to the end)".
    that package was what give us this app we are currently working on right now.


    every page you go to be it homepage or about page as a view function which we creat to direct us to a specific route or pages
     below are some view functions.

    to be able to write a view funtion we have to pass in request into the function and then decide if we want to return and HttpResponse or render the the html file to the browser.

    here is an example  you can try it and see the result you will get from it.

    ##response example below
    -------
    def home(request):
        return HttpResponse("<h1>Home page </h2>")
    ------

    but in this case we are going to be using render method  in stead of HttpResponse method

"""

"""right here we are creating a view functions or function view"""
def home(request):
    return render(request, 'blogapp/index.html')

"""now we have to create a urls.py file in the blogapp folder close to other python files. create the files and lets start working on it."""



def about(request):
    return render(request, 'blogapp/about.html')
