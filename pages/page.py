from selene.support.shared import browser
from Controls.datepicker import Datepicker
from Controls.dropdown import Dropdown
from Controls.tags_input import TagsInput
from data.data import *
from utils.path import absolut_path
from selene.support.shared.jquery_style import s


class RegistrationForm:

    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_mail(self, value):
        browser.element('#userEmail').type(value)
        return self

    def choose_gender(self, value):
        browser.element(f'[for="{value}"]').click()

    def set_phone(self, value):
        browser.element('#userNumber').type(value)
        return self

    def set_date_of_birth(self, year, month, day):
         date_of_birth = Datepicker(s('#dateOfBirthInput'))
         date_of_birth.choose_date(year=year, month=month, day=day)

    def set_subjects(self, value):
        subjects = TagsInput(browser.element('#subjectsInput'))
        subjects.autocomplete(value)
        return self

    def set_hobbie(self, value):
        browser.element(f'[for="{value}"]').click()


    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(absolut_path(value))

    def set_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value):
        state = Dropdown(browser.element('#state')).select(option=value)
        return self

    def set_city(self, value):
        Dropdown(browser.element('#city')).autocomplete(option=value)
        return self

    def submit(self):
        browser.element('#submit').click()


























