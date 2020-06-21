# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
#
# assert 'Django' in browser.title

def test_smoke(selenium):
    selenium.get('http://localhost:8000')

    assert 'Django' in selenium.title