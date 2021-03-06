# Hack Log

I'm violating all the rules Harry put forth in his book. 
I'm using Django 3, 
using a conda environment, 
using an IDE, 
using pytest etc. 
This log is to keep track of what I did differently.

## Preliminaries

Django 3.0.3
pytest
pytest-selenium
pytest-django

## Ch. 1

- `pytest.ini` for pytest discovery.
([ref](https://pytest-django.readthedocs.io/en/latest/tutorial.html#step-2-point-pytest-to-your-django-settings))

- rewrote test to use pytest-selenium.

  - use PyCharm's *Edit Configurations* dropdown to argument **to** add 
    `--driver Firefox`
    
## Ch. 2

- **pytest-selenium** is function-scoped. 
  "Dynamic scope" as of pytest 5.4 was floated as a workaround,
  but not clear how to do this.
  Instead, using 
  [this ref's](https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-with-pytest)
  suggestion to create a class-scoped selenium fixture.
  Note the fixture has to be applied to a base class,
  and any class wanting a single selenium session must inherit from it.
  
## Ch. 3

- urls.py in Django 3 uses django.urls.path
  and not django.conf.urls.url. 
  `path` looks like it avoids regex.
  
## Ch. 4

- creating `testname_old` versions along with `testname` files 
  to separate my pytests from their unittests. 
  
- pytest-django has a `client` fixture alternative to the Django TestCase.client

- To replace Django's TestCase asserts, 
  import their equivalents from pytest_django.asserts.
  PyCharm fails to discover these imports because of the mechanism pytest_django uses.

## Ch. 7

- Since Django 2, models.ForeignKey requires an `on_delete` argument.
  Previously, this defaulted to models.CASCADE, so using this when not specified.
  
- Using a path `<list_id` instead of regex for capture group. 
  Not sure how to capture without assigning a name (`<>` didn't work),
  so turning view_list() arg into a kwarg to allow this.
  
- in urls.py, imported include from django.urls not django.conf.urls

## Ch. 8

- It wasn't necessary, but I used {% load static %} and {% static %} for loading css.

- In the latest bootstrap, offsets are different. 
  Changed `col-md-offset-3` to `offset-md-3` to get centering to work
  and FT formatting test to pass.
  
## Ch. 10

- It looks like uvicorn can be added on top of gunicorn.
  So, will continue with WSGI and then later try to add ASGI.

## Ch. 13

- **django.urls.reverse()** replaces `django.core.urlresolvers.reverse()`
