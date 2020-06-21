from django.test import TestCase
from django.urls import resolve
import pytest

from lists.views import home_page


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    """
    Any class test that wants to use driver_init must inherit from this class.
    """
    pass


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class TestHomePage(BaseTest):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page
