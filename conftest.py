import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init(request):
    class_driver = webdriver.Firefox()
    request.cls.driver = class_driver
    yield
    class_driver.close()
