from selene.support.shared import browser
from selene import be, have
import selene


class DropDown:
    def __init__(self, element: selene.Element):
        self.element = element

    def select(self, option):
        self.element.click()
        browser.all('[id^=react-select][id*=-option-]').element_by(
            have.exact_text(f'{option}')
        ).click()
