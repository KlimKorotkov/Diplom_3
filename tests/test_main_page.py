import allure
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.pages.main_page import MainPage
from Diplom_3.conftest import driver, login, create_and_delete_user


class TestMainPage:
    @allure.title('Проверка появления всплывающее окна после клика по ингредиенту')
    def test_open_ingredient_popup(self, driver):
        MainPage(driver).click_on_bun()
        popup_text = MainPage(driver).get_text_of_element(MainPageLocators.INGREDIENT_POPUP_TITLE)
        assert popup_text == "Детали ингредиента"

    @allure.title('Проверка закрытия всплывающего окна ингредиента кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        MainPage(driver).click_on_bun()
        MainPage(driver).click_close_btn()
        MainPage(driver).check_invisibility(MainPageLocators.INGREDIENT_POPUP)
        assert MainPage(driver).check_element(MainPageLocators.INGREDIENT_POPUP).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        start_quantity = MainPage(driver).check_counter_of_ingredients()
        MainPage(driver).add_filling_to_order_basket()
        end_quantity = MainPage(driver).check_counter_of_ingredients()
        assert end_quantity > start_quantity

    @allure.title('Проверка создания заказа')
    def test_make_order(self, driver, login):
        MainPage(driver).find_element(MainPageLocators.INGREDIENT_BUN)
        MainPage(driver).add_bun_to_order_basket()
        MainPage(driver).add_sauce_to_order_basket()
        MainPage(driver).click_order_btn()
        MainPage(driver).find_element(MainPageLocators.ORDER_NUMBER)
        assert MainPage(driver).check_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
