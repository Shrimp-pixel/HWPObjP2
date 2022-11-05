import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Tuple
import demoqa_tests


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


def format_input_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_input_format)


def format_view_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_view_format)


'''
class User:

    def __init__(self, *, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
'''


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'YouMeanIt'
    email: str = 'abc@efg.com'
    user_number: str = '0123456789'
    birth_day: int = 29
    birth_month: int = 7
    birth_year: int = 1997
    subjects: Tuple[Subject] = (Subject.History,)
    current_address: str = 'bla bla bla'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


yuri = User(name='yuri', gender=Gender.Male)