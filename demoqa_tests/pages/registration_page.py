from selene import browser, be, have, by

from demoqa_tests import resource
from demoqa_tests.data.users import user, user_interests


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, user):
        browser.element("#firstName").should(be.blank).type(user.first_name)
        return self

    def fill_last_name(self, user):
        browser.element("#lastName").should(be.blank).type(user.last_name)
        return self

    def fill_email(self, user):
        browser.element("#userEmail").should(be.blank).type(user.email)
        return self

    def fill_gender(self):
        browser.element("#gender-radio-2").double_click()
        return self

    def fill_user_phone_number(self, user):
        browser.element("#userNumber").should(be.blank).type(user.phone_number)
        return self

    def fill_date_of_birth(self, user):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select").click().element(by.text(user.month_of_birth)).click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(user.year_of_birth)).click()
        browser.element(f'.react-datepicker__day--0{user.day_of_birth}').click()
        return self

    def fill_subject(self, user_interests):
        browser.element("#subjectsInput").type(user_interests.subject).press_enter()
        return self

    def fill_hobby(self):
        browser.element('[for=hobbies-checkbox-1]').click().should(have.text(user_interests.hobby))
        return self

    def fill_upload_pic(self, user):
        browser.element("#uploadPicture").set_value(resource.path(user.photo))
        return self

    def fill_current_address(self, user):
        browser.element("#currentAddress").should(be.blank).type(user.current_address)
        return self

    def fill_state(self, user):
        browser.element("#react-select-3-input").should(be.blank).type(user.state).press_enter()
        return self

    def fill_city(self, user):
        browser.element("#react-select-4-input").should(be.blank).type(user.city).press_enter()
        return self

    def fill_submit_btn(self):
        browser.element("#submit").double_click()
        return self

    def registration(self, user):
        (self
         .fill_first_name(user)
         .fill_last_name(user)
         .fill_email(user)
         .fill_gender()
         .fill_user_phone_number(user)
         .fill_date_of_birth(user)
         .fill_subject(user_interests)
         .fill_hobby()
         .fill_upload_pic(user)
         .fill_current_address(user)
         .fill_state(user)
         .fill_city(user)
         .fill_submit_btn())
        return self

    def check_if_form_was_submitted(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        return self

    def registered_user_data(self):
        return browser.element('.table').all('td').even

    def should_registered_user_contains(self, user, user_interests):
        return browser.element('.table').all('td').even.should(have.texts(f'{user.first_name} {user.last_name}'
                                                                          , user.email, user.gender,
                                                                          f'{user.phone_number}',
                                                                          f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
                                                                          user_interests.subject, user_interests.hobby,
                                                                          user.photo, user.current_address,
                                                                          f'{user.state} {user.city}'))

    def modal_window_check(self, user, user_interests):
        (self
         .check_if_form_was_submitted()
         .should_registered_user_contains(user, user_interests))
        return self
