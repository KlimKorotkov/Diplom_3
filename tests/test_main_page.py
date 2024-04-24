import allure
from Diplom_3.pages.main_page import MainPage
from Diplom_3.conftest import driver, login, create_and_delete_user


class TestMainPage:
    @allure.title('Проверка появления всплывающее окна после клика по ингредиенту')
    def test_open_ingredient_popup(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.click_on_bun()
        popup_text = self.main_page.get_text_of_ingredient_popup_title()
        assert popup_text == "Детали ингредиента"

    @allure.title('Проверка закрытия всплывающего окна ингредиента кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.click_on_bun()
        self.main_page.click_close_btn()
        self.main_page.check_invisibility_ingredient_popup()
        assert self.main_page.check_ingredient_popup().is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        self.main_page = MainPage(driver)
        start_quantity = self.main_page.check_counter_of_ingredients()
        self.main_page.add_filling_to_order_basket()
        end_quantity = self.main_page.check_counter_of_ingredients()
        assert end_quantity > start_quantity

    @allure.title('Проверка создания заказа')
    def test_make_order(self, login, driver):
        self.main_page = MainPage(driver)
        self.main_page.find_ingredient_bun()
        self.main_page.add_bun_to_order_basket()
        self.main_page.add_sauce_to_order_basket()
        self.main_page.click_order_btn()
        self.main_page.find_order_number()
        assert self.main_page.check_order_status_text().is_displayed()
