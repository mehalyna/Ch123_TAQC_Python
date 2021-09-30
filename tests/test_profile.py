import pytest
from allure_commons.types import Severity
import config
from selenium import webdriver


"""
    Testing the 'Profile' page

"""
PROFILE = "Profile"
User = "Username"
New_Name = 'Admin'
Gender_Male = 'Male'
Gender_Female = 'Female'


def test_change_username(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    expected_result = New_Name
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Username')
    admin_setup.profile.input_new_username(New_Name)
    admin_setup.profile.username_submit_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Username')
    assert expected_result == admin_setup.profile.check_new_username()

def test_change_username_clear_field(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Username')
    admin_setup.profile.input_new_username(New_Name)
    admin_setup.profile.username_clear_btn.click_btn_by_css()
    admin_setup.profile.input_new_username('Add')
    admin_setup.profile.username_clear_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Username')
    #assert expected_result == admin_setup.profile.check_new_username()

def test_gender_male(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    expected_result = Gender_Male
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Gender')
    admin_setup.profile.change_gender_option(Gender_Male)
    admin_setup.profile.gender_submit_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Gender')
    assert expected_result == admin_setup.profile.check_new_gender()

def test_gender_female(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    expected_result = Gender_Female
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Gender')
    admin_setup.profile.change_gender_option(Gender_Female)
    admin_setup.profile.gender_submit_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Gender')
    assert expected_result == admin_setup.profile.check_new_gender()


def test_change_date_of_birth(admin_setup):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Date of Birth')
    admin_setup.profile.expansion_panel_date_of_birth_dtp.write_date_to_datepicker(10, 10, 2000)
    #admin_setup.profile.date_of_birth_submit_btn.click_btn_by_css()


def test_choose_categories(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Favorite Categories')
    admin_setup.profile.choose_favorite_categories('Sea')

def test_change_password(admin_setup):
    # with allure.step('Переходимо на сторінку логування'):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.navigation.navigation_edit_profile_btn.click_btn_by_css()
    admin_setup.profile.expansion_panel_by_name_btn.click_btn_by_name('Change Password')
    admin_setup.profile.change_password(34,56,45)
    admin_setup.profile.password_clear_btn.click_btn_by_css()