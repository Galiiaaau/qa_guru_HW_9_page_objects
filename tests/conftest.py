import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1500

    yield
    browser.quit()
