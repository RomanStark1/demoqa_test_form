from selene.support.shared import browser
from selene import be, have
import pytest
import random
import os
from selene.support.shared.jquery_style import s
from Controls.check_final_table import FinalTable
from Controls.datepicker import Datepicker
from Controls.dropdown import Dropdown
from data.data import *
from utils.path import absolut_path
from utils.remove_element import remove_element
from Controls.tags_input import TagsInput


@pytest.fixture(scope='session', autouse=True)
def config():
    browser.config.hold_browser_open = True



