from selene import have
import selene


class CheckBox:
    def __init__(self, elements: selene.Collection):
        self.elements = elements

    def check_options(self, *options: str):
        for option in options:
            self.elements.by(have.exact_text(option)).first.element('..').click()
