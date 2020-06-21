from django.http import HttpRequest
from django.urls import resolve  # finds the function a URL maps to
import pytest

from lists.views import home_page


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    """
    Any class test that wants to use driver_init must inherit from this class.
    """
    pass


class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        assert html.startswith('<html>')
        assert '<title>To-Do lists</title>' in html
        assert html.strip().endswith('</html>')
