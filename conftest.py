import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language. For example: en, fr, ru or other')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language is not None:
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(6)
    else:
        raise pytest.UsageError('--language should be implemented')
    yield browser
    browser.quit()