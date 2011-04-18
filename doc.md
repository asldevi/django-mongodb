
A simple app with Django using MongoDB
--------------------------------------

MongoDB is fairly easy-to-use nosql database and the python module `mongoengine` makes the life even better to work with `mongodb` from python. So, once django, mongodb and mongoengine are installed, let's see how we can make a simple app that takes a comment, commenter's name, stores them and displays back 4 per page.

As for any django app, first make a project with

    $ django-admin.py startproject django-mongodb
    $ cd django-mongodb

Edit settings.py to remove all the default `INSTALLED_APPS` and configure database settings. Here comes the not so straight-forward thing to do.  As per intuition, one tends to keep `ENGINE` as `django.db.backends.mongodb` in DATABASES and expects things to work. But there is no such thing as `mongodb` or `mongo` in `django.db.backends`. The `mongoengine` website says not to bother about the DATABASES dict at all and having `mongoengine.connect(db_name)` somewhere in the `settings.py` will work. With that in place, django complaints that you haven't set the database and hence can't do `syncdb` successfully.

Now, what's the solution? Well, just keep `django.db.backends.sqlite3` as the engine with some dummy name and do the `mongoengine.connect`. Django no more complains when you run `syncdb`, in fact it creates both the sqlite database (empty) and mongodb database, provided you have mongod running up and sqlite3 installed. 

Once the db connections are done, add `comments` in `INSTALLED_APPS` and run 

    $ python manage.py startapp comments

That creates `comments` dir in cwd which has views.py, models.py in it. Usually in models.py we write classes that extend from django.db.models.Model and django figures out how to create db schema for them. With mongoengine, mongoengine.Document extends Model and it suffices for us to extend our models from Document. Writing urls and views are the regular tasks as in any other django app. For the POST requests, django uses `csrf_token` as a security measure against CSRF attacks -  so, one shouldn't miss that out in sending post request as well as in the template.  Lastly, django's Paginator module comes very handy for pagination. Some basic javascript form validation makes it work better and it comes for free with jquery.validate.js, which works like a charm. That's it - we're ready with the comments app! 

Now, for the deployment, we have fabulous `Fabric`. The time spent with fabric pays us very quickly - when you deploy on a clean slate and test you don't need to remember the sequence of commands or the args to them. What a savior!