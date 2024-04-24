import allure
from Diplom_3.data import Urls
from Diplom_3.pages.user_account_page import UserAccountPage
from Diplom_3.pages.password_recovery_page import PasswordRecoverPage
from Diplom_3.pages.header_page import HeaderPage
from Diplom_3.conftest import driver, create_and_delete_user


class TestPasswordRecover:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_recover_button(self, driver):
        self.password_recovery_page = PasswordRecoverPage(driver)
        HeaderPage(driver).click_user_account_btn()
        UserAccountPage(driver).click_password_recover_btn()
        self.password_recovery_page.click_recover_btn()
        assert self.password_recovery_page.find_save_btn().is_displayed()

    @allure.title('Проверка перехода по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_recover(self, create_and_delete_user, driver):
        self.password_recovery_page = PasswordRecoverPage(driver)
        self.password_recovery_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        self.password_recovery_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        self.password_recovery_page.click_recover_btn()
        assert self.password_recovery_page.find_save_btn().is_displayed()

    @allure.title('Проверка активности поля пароль после клика по иконке показать/скрыть')
    def test_active_password_field(self, create_and_delete_user, driver):
        self.password_recovery_page = PasswordRecoverPage(driver)
        self.password_recovery_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        self.password_recovery_page.set_email_for_recover_password(create_and_delete_user[0]['email'])
        self.password_recovery_page.click_recover_btn()
        self.password_recovery_page.find_save_btn()
        self.password_recovery_page.click_on_show_password_icon()
        assert self.password_recovery_page.find_input_password_active()
