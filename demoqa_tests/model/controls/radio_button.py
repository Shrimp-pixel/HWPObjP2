from selene.support.shared import browser
from selene import have, command


class RadioButton:
    def __init__(self, browser_all):
        self.browser_all = browser_all

    def set_option(self, value):
        # browser.element(f'[for={label_prefix}-radio-{number}]').click()
        self.browser_all.element_by(have.text(value)).click()
