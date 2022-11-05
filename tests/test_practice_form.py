import datetime

from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.model.data import user
from demoqa_tests.model.data.user import User, Gender


def test_submit_filled_form():
    (
        app.practice_page.open()

        .fill_name('Lev', 'Zavodskov')
        .fill_email('lev@zavodskov.xyz')
        .fill_gender(user.Gender.Male)
        .fill_birthday(datetime.date(1997, 7, 29))
        .fill_phone('7000000000')
        .fill_subjects('Maths', 'English', 'Computer Science')
        .fill_hobbies(user.Hobby.Music, user.Hobby.Reading)
        .select_picture('picture.png')
        .fill_address('Country/State/City/Street/ Street num')
        .select_state('NCR')
        .select_city('Gurgaon')
        .submit_form()

        .assert_form_sent(
            ('Student Name', 'Lev Zavodskov'),
            ('Student Email', 'lev@zavodskov.xyz'),
            ('Gender', Gender.Male.value),
            ('Mobile', '7000000000'),
            ('Date of Birth', datetime.date(1997, 7, 29)),
            ('Subjects', 'Maths, English, Computer Science'),
            ('Hobbies', f'{user.Hobby.Music.value}, {user.Hobby.Reading.value}'),
            ('Picture', 'picture.png'),
            ('Address', 'Country/State/City/Street/ Street num'),
            ('State and City', 'NCR Gurgaon'),
        )
    )


def test_submit_filled_form_():

    lev = User(
        name='Lev',
        last_name='Zavodskov',
        email='lev@zavoskov.xyz',
        gender=Gender.Male,
    )

    app.practice_page.open().register(lev).assert_registered(lev)


