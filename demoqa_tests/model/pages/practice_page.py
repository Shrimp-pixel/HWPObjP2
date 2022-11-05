from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model import google
from demoqa_tests.model.controls import (
    dropdown,
    radio_button,
    checkbox,
    file_input,
)
from demoqa_tests.model.components import modal
from selene import command, have

from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.checkbox import CheckBox
from demoqa_tests.model.controls.dropdown import DropDown
from demoqa_tests.model.controls.file_input import FileInput
from demoqa_tests.model.controls.radio_button import RadioButton
from demoqa_tests.model.data import user
import datetime
from demoqa_tests import have
from demoqa_tests.utils.selene import command

class PracticePage:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))
        self.checkbox = CheckBox(browser.all('[for^=hobbies-checkbox]'))
        self.dropdown_city = DropDown(browser.element('#city'))
        self.dropdown_state = DropDown(browser.element('#state'))
        self.file_input = FileInput(browser.element('#uploadPicture'))
        self.radio_button = RadioButton(browser.all(f'[for^=gender-radio]'))

    def open(self):  # noqa
        browser.open('/automation-practice-form')
        google.remove_ads(amount=3, timeout=6)
        google.remove_ads(amount=1, timeout=2)
        return self

    def fill_name(self, firstname: str, lastname: str):
        browser.element('#firstName').type(firstname)
        browser.element('#lastName').type(lastname)
        return self

    def fill_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def fill_phone(self, phone: str):
        browser.element('#userNumber').type(phone)
        return self

    def fill_subjects(self, *subjects: str):
        for item in subjects:
            browser.element('#subjectsInput').type(item).press_enter()
        return self

    def fill_hobbies(self, *options: user.Hobby):
        print(type(browser.all('[for^=hobbies-checkbox]')))
        self.checkbox.check_options(
           *[option.value for option in options]
        )
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, state: str):
        utils.browser.scroll_one_page()
        self.dropdown_state.select(state)
        return self

    def select_city(self, city: str):
        self.dropdown_city.select(city)
        return self

    def submit_form(self):
        # utils.browser.scroll_one_page()
        # browser.element('#submit').click()
        browser.element('#submit').perform(command.js.click)
        return self

    def assert_form_sent(self, *data):
        for name, value in data:
            value = (
                user.format_view_date(value) if isinstance(value, datetime.date) else value
            )
            modal.rows.element_by(have.text(name)).all('td')[1].should(
                have.exact_text(value)
            )
        return self

    def fill_gender(self, value: user.Gender):
        # radio_button.set_option('gender', value.value)

        self.radio_button.set_option(value.value)  # noqa

        return self

    def fill_birthday(self, date: datetime.date):
        self.birthday.set_date(date)
        return self

    def assert_filled_birthday(self, date: datetime.date):
        # birthday.should(have.date(date))
        self.birthday.assert_value(date)
        # """
        # just an example for advocates of including assertions into PageObjects
        # see https://martinfowler.com/bliki/PageObject.html for more details
        # """
        return self

    def select_picture(self, file_name):
        self.file_input.upload(f'../resources/{file_name}')
        return self

    def register(self, user_data):
        self.fill_name(user_data.name, user_data.last_name)
        self.fill_email(user_data.email)
        self.fill_gender(user_data.gender)
        self.fill_birthday(datetime.date(user_data.birth_year, user_data.birth_month, user_data.birth_day))
        self.fill_phone(user_data.user_number)
        self.fill_subjects(*[subject.value for subject in user_data.subjects])
        self.fill_hobbies(*user_data.hobbies)
        self.select_picture(user_data.picture_file)
        self.fill_address(user_data.current_address)
        self.select_state(user_data.state)
        self.select_city(user_data.city)
        self.submit_form()
        return self

    def assert_registered(self, user_data):
        self.assert_form_sent(
            ('Student Name', f'{user_data.name} {user_data.last_name}'),
            ('Student Email', user_data.email),
            ('Gender', user_data.gender.value),
            ('Mobile', user_data.user_number),
            ('Date of Birth', datetime.date(user_data.birth_year, user_data.birth_month, user_data.birth_day)),
            ('Subjects', *[subject.value for subject in user_data.subjects]),
            ('Hobbies', *[hobbiy.value for hobbiy in user_data.hobbies]),
            ('Picture', user_data.picture_file),
            ('Address', user_data.current_address),
            ('State and City', f'{user_data.state} {user_data.city}'),
        )
        return self
