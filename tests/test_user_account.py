import allure
from Diplom_3.data import Urls
from Diplom_3.locators.user_account_locators import UserAccountLocators
from Diplom_3.pages.user_account_page import UserAccountPage
from Diplom_3.pages.header_page import HeaderPage
from Diplom_3.conftest import driver, login, create_and_delete_user


class TestUserAccount:
    def setup_class_user_account_page(self):
        self.user_account_page = UserAccountPage(driver)

    @allure.title('Проверка перехода в личный кабинет через кнопку "Личный кабинет" в шапке')
    def test_redirect_to_account_from_header(self, login):
        self.user_account_page.click_account_btn()
        assert self.user_account_page.get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел История заказов')
    def test_redirect_to_order_history(self, login):
        self.user_account_page.click_account_btn()
        self.user_account_page.click_on_order_list()
        assert self.user_account_page.get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        HeaderPage(driver).click_user_account_btn()
        self.user_account_page.wait_visibility_element(UserAccountLocators.PROFILE_BTN)
        self.user_account_page.click_logout_btn()
        self.user_account_page.wait_visibility_element(UserAccountLocators.ENTER_BTN)
        btn_text = self.user_account_page.get_text_of_element(UserAccountLocators.ENTER_BTN)
        assert btn_text == 'Войти'
