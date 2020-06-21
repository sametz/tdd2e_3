import pytest


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    """
    Any class test that wants to use driver_init must inherit from this class.
    """
    pass


def test_smoke(selenium):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    selenium.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    assert 'To-Do' in selenium.title


class TestNewVisitorTest(BaseTest):
    def test_smoke(self):
        assert 1 == 1

    def test_fixture(self):
        self.driver.get('http://localhost:8000')
        assert 'Django' in self.driver.title
