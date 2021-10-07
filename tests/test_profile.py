import pytest
from allure_commons.types import Severity
import config
from selenium import webdriver
import allure


"""
    Testing the 'Profile' page

"""
PROFILE = "Profile"
USER = "Username"
NEW_NAME = 'Admin'
NEW_NAME2 = 'Check'
GENDER_MALE = 'Male'
GENDER_FENALE = 'Female'
GENDER = 'Gender'
SEA = "Sea"
MOUNT = "Mount"



@allure.title("Test test_change_username:")
@allure.severity(Severity.NORMAL)
def test_change_username(admin_setup):
    """
            Verify that user has the ability to change username.
    """
    with allure.step("Click find event button and go to edit profile page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    with allure.step("Input new user name "):
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(USER)
        admin_setup.profile.input_new_username(NEW_NAME)
    with allure.step("Click submit button"):
        admin_setup.profile.username_submit_btn.click_btn_by_css()
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(USER)
    with allure.step("Verify that name is changed"):
        assert NEW_NAME == admin_setup.profile.get_new_username()

@allure.title("Test test change username clear field:")
@allure.severity(Severity.NORMAL)
def test_change_username_clear_field(admin_setup):
    """
            Verify that buttin 'CLEAR' clear all the fields.
    """
    with allure.step("Click find event button and go to edit profile page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    with allure.step("Input new user name "):
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(USER)
        admin_setup.profile.input_new_username(NEW_NAME2)
    with allure.step("Click clear button"):
        admin_setup.profile.username_clear_btn.click_btn_by_css()
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(USER)
    with allure.step("Verify that name is not changed and field is empty"):
        assert NEW_NAME2 != admin_setup.profile.get_new_username()

@allure.title("Test test change gender:")
@allure.severity(Severity.NORMAL)
def test_gender(admin_setup):
    """
        Verify that user has the ability to change gender.
    """
    expected_result = GENDER_MALE
    with allure.step("Click find event button and go to edit profile page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    with allure.step("Select Male option from drop down menu"):
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(GENDER)
        admin_setup.profile.change_gender_option(GENDER_MALE)
    with allure.step("Click submit button"):
        admin_setup.profile.gender_submit_btn.click_btn_by_css()
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css(GENDER)
    with allure.step("Verify that gender is changed"):
        assert expected_result == admin_setup.profile.get_new_gender()

@allure.title("Test test change date of birth:")
@allure.severity(Severity.NORMAL)
def test_change_date_of_birth(admin_setup):
    """
            Verify that user has the ability to change date of birth.
    """
    with allure.step("Click find event button and go to edit profile page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css('Date of Birth')
    with allure.step("Filling datepickers"):
        admin_setup.profile.expansion_panel_date_of_birth_dtp.write_date_to_datepicker(10, 8, 2001)
    with allure.step("Verify that the date changed"):
        assert '10 Oct 2002' == admin_setup.profile.get_new_date_of_birth()


@allure.title("Test test warning wrong password:")
@allure.severity(Severity.NORMAL)
def test_warning_wrong_password(admin_setup):
    """
                Verify that user warning about wrong password appear.
    """
    with allure.step("Click find event button and go to edit profile page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
        admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    with allure.step("Input wrong current password and new password "):
        admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name_by_css('Change Password')
        admin_setup.profile.change_password('aed', 56, 45)
    with allure.step("Click submit button"):
        admin_setup.profile.password_submit_btn.click_btn_by_css()
    with allure.step("Check if there are a warning"):
        assert admin_setup.profile.warning_wrong_password() == 'Wrong password'

