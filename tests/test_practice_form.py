from selene import have
from demoqa_tests.pages.registration_page import RegistrationPage


def test_fill_out_the_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # Filling out the form
    registration_page.fill_first_name("Galiia")
    registration_page.fill_last_name("Uzbekova")
    registration_page.fill_email("galiiauzbekova@gmail.com")
    registration_page.fill_gender()
    registration_page.fill_user_phone_number("8937365074")
    registration_page.fill_date_of_birth('1994', 'February', '18')
    registration_page.fill_subject("English")
    registration_page.fill_hobby()
    registration_page.fill_upload_pic("this-is-fine.png")
    registration_page.fill_current_address("Moscow")
    registration_page.fill_state("NCR")
    registration_page.fill_city("Delhi")
    registration_page.fill_submit_btn()

    # Check if the form was submitted
    registration_page.check_if_form_was_submitted("Thanks for submitting the form")

    # Check if the results are correct
    registration_page.registered_user_data().should(
        have.exact_texts(
            "Galiia Uzbekova",
            "galiiauzbekova@gmail.com",
            "Female",
            "8937365074",
            "18 February,1994",
            "English",
            "Reading",
            "this-is-fine.png",
            "Moscow",
            "NCR Delhi"
        ))
