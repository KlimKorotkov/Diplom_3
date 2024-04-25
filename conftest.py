import pytest
from selenium import webdriver
from Diplom_3.helpers import *
from Diplom_3.locators.user_account_locators import UserAccountLocators
from Diplom_3.locators.header_locators import HeaderLocators
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.user_account_page import UserAccountPage
import requests
from Diplom_3.data import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def create_and_delete_user():

    name = generate_random_string(10)
    email = generate_random_string(10)+'@yandex.ru'
    password = generate_random_string(10)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Urls.REGISTER_USER, data=payload)
    access_token = response.json()["accessToken"]
    yield login_data, access_token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def login(driver, create_and_delete_user):
    email = create_and_delete_user[0]['email']
    password = create_and_delete_user[0]['password']

    main_page = MainPage(driver)
    main_page.click_on_enter_btn()
    main_page.click_on_account_btn()

    account_page = UserAccountPage(driver)
    account_page.login(email, password)