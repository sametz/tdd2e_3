# Notes to myself on how Django works.

## Basics

- follow `python manage.py` with:
  - runserver to run the test server
  - test to run Django unittests
  - startapp {name} to create a new app
    - need to add app name to `INSTALLED_APPS` in `settings.py`
  - collectstatic to collect all static files into the STATIC_ROOT folder
## Flow

- an incoming request is parsed by `urls.py`
  and matched to a view function
- the view function is called with a 
  django.http.HttpRequest object as argument
- the view function parses the request.
  - It can return a rendering of the page 
    (e.g. django.shortcuts.render)
  - it can perform tasks 
    (e.g. handle POST request)
    and then redirect

## Template language

- `{% csrf_token %}` security token for POSTs
- render(request, filename, kwargs): the keys can be used as variables in templates.
e.g. with kwargs `{'new_item_text': 'foo'}`:
  ```jinja2
  {{ new_item_text }} 
  ```
  will be rendered as "foo".
- with `items` passed in as key:
  ```jinja2
  {% for item in items %}
    <tr><td>{{ item.text }}</td></tr>
  {% endfor %}
  ```
- The loop counter can be referenced by `{{ forloop.counter }}`. 
  Note: index appears to start at 1, not 0.
## DB

- models.py define the data structure
- `python manage.py makemigrations` generates .py files in migrations folder.
  Tells Django you made changes to your models.
- `python manage.py migrate` makes those changes to the DB
  - if you want to trash the DB and start over,
  `rm db.sqlite3` and migrate again
  
## Django API

### django.db.models

- `.TextField()`
- **.ForeignKey(model, on_delete, \*\*kwargs)** is used to relate a model to another model.
  **DJANGO 3**: on_delete is required since Django 2. 
  It previously defaulted to models.CASCADE.

#### django.db.models.Model

##### `.objects`

- see [Retrieving Objects](https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-objects)
- "To retrieve objects from your database, construct a QuerySet via a Manager on your model class."
  - a QuerySet represents a collection of objects from your database
  - you get a QuerySet by using your model's Manager.
    - Each model has at least one Manager, and it's called `objects` by default.

Methods on Model.objects:
- `.all()` returns a QuerySet of all the objects in the database.
- `.count()` returns # of records in QuerySet
- `.first()` returns first object matched
- `.create(**kwargs)` creates a new record

### django.http

Request and response objects pass state through the system.

#### HttpRequest

- .method gives 'GET', 'POST' etc
- .POST is a dict-like object

#### HttpResponse

- can instantiate with the actual HTML as string
- .content.decode('utf8') gives HTML

### django.shortcuts

#### django.shortcuts.redirect

- `redirect(path: str)` returns an **HttpResponseRedirect** object

#### django.shortcuts.render

- takes a request and a template name as required arguments
- returns an HttpResponse object

### django.urls.resolve

- Takes a text path as argument 
  and returns a ResolverMatch object with metadata on the resolved URL.
  - .func attribute returns the view function used 
- combines a given template with a given context directory
  and returns an HttpResponse object with that
  rendered text

## django.tests API

### TestCase

- asserts:
  - assertTemplateUsed(response: Response, filename.html: string)
  - assertContains(response, string): 
    more concise than using assertIn and response.content.decode()
  - assertRedirects(response, string)

#### TestCase.client

- like Django's own headless Selenium
  - pytest has a client fixture that basically borrows this
- unlike Selenium, does NOT require web server to be running.
  Only interacts with Django framework
  - test that correct templates are rendered
  - test that template is passed correct context data
  - use Selenium to test *rendering* of HTML and JS
- `.get(path: string)`: returns a Response object
- `.postpath: string, {}`: returns a Response object
  
### The Response object

- the Response object is **not** an HttpResponse but is tailored for testing
- can be used in asserts, e.g.: 
  - .assertTemplateUsed(response, filename)
  - .assertIn(string, response.content.decode())
- `response.status_code` returns status code
- `response['location']` e.g. shows destination URL in a redirect response

### LiveServerTestCase

Allows functional tests to be run via **manager.py**
and not muck with the live DB.

## Selenium reminders

- uses a selenium.webdriver object
- `.get(url)`: loads the page
- `.find_element(s)_by_{tag_name | id`}:
returns a WebElement object
- `.quit()`

### selenium.webdriver.common.keys.Keys

### selenium.webdriver.remote.webelement.WebElement

- `.get_attribute('{attrubute}')`
- `.send_keys({string | Keys})`