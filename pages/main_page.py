import allure
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.header_locators import HeaderLocators
from Diplom_3.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_enter_btn(self):
        self.move_to_element_and_click(MainPageLocators.ENTER_ACCOUNT_BTN)

    @allure.step('Клик по ингредиенту "Флюоресцентная булка"')
    def click_on_bun(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Клик по крестику в модальном окне')
    def click_close_btn(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_order_btn(self):
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)

    @allure.step('Добавление булки в корзину')
    def add_bun_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление начинки в корзину')
    def add_filling_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)

    @allure.step('Добавление соуса в корзину')
    def add_sauce_to_order_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_SAUCE, MainPageLocators.ORDER_BASKET)

    @allure.step('Получение количества добавленного ингредиента')
    def check_counter_of_ingredients(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Создание заказа и получение его номера')
    def make_order_and_get_order_number(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN, MainPageLocators.ORDER_BASKET)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FILLING, MainPageLocators.ORDER_BASKET)
        self.find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.move_to_element_and_click(MainPageLocators.CREATE_ORDER_BTN)
        self.wait_visibility_element(MainPageLocators.ORDER_STATUS_TEXT)
        self.wait_invisibility_element(MainPageLocators.DEFAULT_ORDER_NUMBER)
        order = self.get_text_of_element(MainPageLocators.ORDER_NUMBER)
        self.move_to_element_and_click(MainPageLocators.CLOSE_BTN)
        return order

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_btn(self):
        self.move_to_element_and_click(HeaderLocators.ACCOUNT_BTN)

    @allure.step('Получение текста элемента')
    def get_text_of_ingredient_popup_title(self):
        return self.driver.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).text

    @allure.step('Проверка невидимости элемента на странице')
    def check_invisibility_ingredient_popup(self):
        return self.driver.check_invisibility(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Проверка отображения элемента на странице')
    def check_ingredient_popup(self):
        self.driver.check_element(MainPageLocators.INGREDIENT_POPUP)
        return self.driver.find_element(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Поиск элемента')
    def find_ingredient_bun(self):
        return self.driver.find_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Поиск элемента')
    def find_order_number(self):
        return self.driver.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Проверка отображения элемента на странице')
    def check_order_status_text(self):
        self.driver.check_element(MainPageLocators.ORDER_STATUS_TEXT)
        return self.driver.find_element(MainPageLocators.ORDER_STATUS_TEXT)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_burger_constructor_title(self):
        self.driver.find_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)
