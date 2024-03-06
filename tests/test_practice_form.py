from demoqa_tests.data.users import user, user_interests
from demoqa_tests.pages.registration_page import RegistrationPage


def test_fill_out_the_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # Filling out the form
    registration_page.registration(user)
    registration_page.modal_window_check(user, user_interests)
