from selene.support.shared import browser
import os
import selene


class FileInput:
    def __init__(self, element: selene.Element):
        self.element = element

    def upload(self, relative_path):
        self.element.send_keys(os.path.abspath(relative_path))
