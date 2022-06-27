from selene.support.shared import browser
from selene import be, have
import pytest
import random

@pytest.fixture(scope='session', autouse=True)
def config():
    browser.config.hold_browser_open = True



