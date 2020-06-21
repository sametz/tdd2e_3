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
