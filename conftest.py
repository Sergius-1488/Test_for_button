import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # , action='store', default=None, )
    parser.addoption("--language", default="ru")
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    # 'es'}) #сюда запихнуть выбранный язык
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    browser_name = request.config.getoption("browser")
    driver = None
    if browser_name == "chrome":
        print("\nstart browser for test..")
        driver = webdriver.Chrome(options=options)
    time.sleep(5)
    yield driver
    print("\nquit browser..")
    driver.quit()
