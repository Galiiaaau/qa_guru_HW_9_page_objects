from selene import browser, be, have, by

from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, first_name):
        browser.element("#firstName").should(be.blank).type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").should(be.blank).type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").should(be.blank).type(email)

    def fill_gender(self):
        browser.element("#gender-radio-2").double_click()

    def fill_user_phone_number(self, user_phone_number):
        browser.element("#userNumber").should(be.blank).type(user_phone_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select").click().element(by.text(month)).click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, subject):
        browser.element("#subjectsInput").type(subject).press_enter()

    def fill_hobby(self):
        browser.element('[for=hobbies-checkbox-2]').click()

    def fill_upload_pic(self, name_of_pic):
        browser.element("#uploadPicture").set_value(resource.path(name_of_pic))

    def fill_current_address(self, current_address):
        browser.element("#currentAddress").should(be.blank).type(current_address)

    def fill_state(self, state):
        browser.element("#react-select-3-input").should(be.blank).type(state).press_enter()

    def fill_city(self, city):
        browser.element("#react-select-4-input").should(be.blank).type(city).press_enter()

    def fill_submit_btn(self):
        browser.element("#submit").double_click()

    def check_if_form_was_submitted(self, value):
        browser.element("#example-modal-sizes-title-lg").should(have.text(value))

    def registered_user_data(self):
        return browser.element('.table').all('td').even
