import pytest
# pytest_django.asserts has versions of Django TestCase assersions,
# but note that PyTest can't discover them and will flag them.
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    """
    Any class test that wants to use driver_init must inherit from this class.
    """
    pass


@pytest.mark.client  # use pytest_django 'client' fixture instead of django TestCase's
class TestHomePage:

    def test_uses_home_template(self, client):
        response = client.get('/')
        assertTemplateUsed(response, 'home.html')
