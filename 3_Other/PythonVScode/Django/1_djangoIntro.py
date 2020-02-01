# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:41:07 2018

@author: SilverDoe
"""

# pip install Django
import django
print(django.get_version())

''' in cmd type :

python -m django --version

=========== create a django project ============================================

If this is your first time using Django, you’ll have to take care of some initial setup.
Namely, you’ll need to auto-generate some code that establishes a Django project – a collection
of settings for an instance of Django, including database configuration, Django-specific 
options and application-specific settings.

>> change your working directory in cmd if you want to save the project in a specific location.
'''

django-admin startproject mysite # cmd command to create a project

'''
These are the files that are auto-generated in the working directory after executing the above command :
========================================================================================================

The outer mysite/ root directory is just a container for your project. Its name doesn’t 
matter to Django; you can rename it to anything you like.

manage.py: A command-line utility that lets you interact with this Django project in 
various ways. You can read all the details about manage.py in django-admin and manage.py.

The inner mysite/ directory is the actual Python package for your project. Its name is the
 Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
 
mysite/__init__.py: An empty file that tells Python that this directory should be considered
a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your
jango-powered site. You can read more about URLs in URL dispatcher.

mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


'''

'''
Let’s verify whether your Django project works. Change into the outer mysite directory, if you haven’t
already, and run the following commands:

'''
python manage.py runserver # command to start the Django development server


'''===================== Changing the port ====================================

>> By default, the runserver command starts the development server on the internal IP at port 8000.
If you want to change the server’s port, pass it as a command-line argument. For instance,
this command starts the server on port 8080 : 
    
'''

python manage.py runserver 8080

'''

If you want to change the server’s IP, pass it along with the port. For example, to
listen on all available public IPs (which is useful if you are running Vagrant or 
want to show off your work on other computers on the network), use:    
    
'''
python manage.py runserver 0:8000

'''
0 is a shortcut for 0.0.0.0. Full docs for the development server can be found in the runserver reference.

Note :The development server automatically reloads Python code for each request as needed.
You don’t need to restart the server for code changes to take effect. However, some actions
 like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

'''


'''

=================== creating an app ================================================================

Your apps can live anywhere on your Python path. In this tutorial, we’ll create our poll app right next to
your manage.py file so that it can be imported as its own top-level module, rather than a submodule of mysite.

To create your app, make sure you’re in the same directory as manage.py and type this command:

'''
 python manage.py startapp polls

'''

========================= Write your first view ===========================

Let’s write the first view. Open the file polls/views.py and put the following Python code in it:
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''
 To call the view, we need to map it to a URL - and for this we need a URLconf.

 ================ Create urls for view ====================================

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

In the polls/urls.py file include the following code:

'''

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

'''
The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py,
add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:


'''

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

'''

The include() function allows referencing other URLconfs. Whenever Django encounters include(), 
it chops off whatever part of the URL matched up to that point and sends the remaining string to
 the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own 
URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under 
“/content/polls/”, or any other path root, and the app will still work.
'''





























































