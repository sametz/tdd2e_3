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
