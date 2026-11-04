import time
import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        # Configuração correta para ativar os logs de performance exigidos pelo helpers.py
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_call_taxi()
        assert self.driver.find_element(*UrbanRoutesPage.from_field).get_property('value') == data.ADDRESS_FROM
        assert self.driver.find_element(*UrbanRoutesPage.to_field).get_property('value') == data.ADDRESS_TO

    def test_select_plan(self):
        self.routes_page.select_comfort_tariff()

    def test_fill_phone_number(self):
        self.routes_page.set_phone(data.PHONE_NUMBER)
        time.sleep(3)  # Aguarda a requisição do SMS ser disparada
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_code(phone_code)

    def test_fill_card(self):
        self.routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)

    def test_comment_for_driver(self):
        self.routes_page.set_comment(data.MESSAGE_FOR_DRIVER)
        assert self.driver.find_element(*UrbanRoutesPage.message_field).get_property('value') == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.order_blanket_and_handkerchiefs()
        assert self.driver.find_element(*UrbanRoutesPage.blanket_checkbox).is_selected()

    def test_order_2_ice_creams(self):
        self.routes_page.order_2_ice_creams()
        assert self.driver.find_element(*UrbanRoutesPage.ice_cream_value).text == '2'

    def test_car_search_model_appears(self):
        self.routes_page.click_final_order()
        assert self.routes_page.is_car_search_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()