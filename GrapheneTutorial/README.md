# Django/GraphQL integration using Graphene #

Tested with Python (3.5 and 2.7.12) and the latest stable version for the following packages.

pip list:
* Django (1.10.5)
* django-filter (1.0.1)
* django-graphiql (0.4.4)
* graphene (1.1.3)
* graphene-django (1.2.1)
* graphql-core (1.0.1)
* graphql-relay (0.4.5)

I strongly recommend using _virtualenv_ and _virtualenvwrapper_

## Installation Notes ##

### Install the source ###
* Clone or download this repository.
* run *pip install -r requirements.txt*

### Generate and run migration scripts ###
* python manage.py makemigrations
* python manage.py migrate

### Load some test data into your data store ###

* python manage.py loaddata courses

### Run the application and test GraphQL ###

* python manage.py runserver
* Go to **http://localhost:8000/graphql**

## Check the tutorial ##

[Part 1 - Integration and Basic Queries](http://arecordon.blogspot.com.ar/2017/01/django-graphql-integration-with-graphene_24.html)

[Part 2 - Mutations](http://arecordon.blogspot.com.ar/2017/01/django-graphql-integration-with.html)
