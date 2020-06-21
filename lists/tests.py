from django.test import TestCase
import pytest


@pytest.mark.usefixtures('driver_init')
class BaseTest:
    """
    Any class test that wants to use driver_init must inherit from this class.
    """
    pass


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)


class TestSmoke(BaseTest):

    def test_bad_maths(self):
        assert 1 + 1 == 3
