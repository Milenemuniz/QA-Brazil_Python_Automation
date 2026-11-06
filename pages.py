from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_call_taxi = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff = (By.XPATH, '//div[text()="Comfort"]')

    phone_button = (By.CLASS_NAME, 'np-button')
    phone_input = (By.ID, 'phone')
    phone_submit_button = (By.XPATH, '//button[text()="Próximo"]')
    code_input = (By.ID, 'code')
    # Seletor ajustado para aceitar tanto "Confirmar" quanto "Confirm"
    code_submit_button = (By.XPATH, '//button[text()="Confirmar" or text()="Confirm"]')

    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus-container')

    card_number_input = (By.XPATH, '//div[contains(@class, "payment-picker")]//input[@id="number"]')
    card_code_input = (By.XPATH, '//div[contains(@class, "payment-picker")]//input[@id="code"]')

    card_close_button = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button button"]')

    message_field = (By.ID, 'comment')

    blanket_switch = (By.XPATH, '//div[contains(text(), "Cobertor") or contains(text(), "Blanket")]/..//span[@class="slider round"]')
    blanket_checkbox = (By.XPATH, '//div[contains(text(), "Cobertor") or contains(text(), "Blanket")]/..//input[@type="checkbox"]')

    ice_cream_plus = (By.XPATH,
                      '//div[text()="Sorvete" or contains(text(), "Ice cream")]/..//div[@class="counter-plus"]')
    ice_cream_value = (By.XPATH,
                       '//div[text()="Sorvete" or contains(text(), "Ice cream")]/..//div[@class="counter-value"]')

    order_button = (By.CLASS_NAME, 'smart-button')
    car_search_modal = (By.CLASS_NAME, 'order-body')
    overlay_element = (By.CLASS_NAME, 'overlay')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_overlay(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(self.overlay_element)
            )
        except:
            pass

    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def click_call_taxi(self):
        time.sleep(1)
        self.driver.find_element(*self.button_call_taxi).click()

    def select_comfort_tariff(self):
        self.wait_for_overlay()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.comfort_tariff))
        self.driver.execute_script("arguments[0].click();", element)

    def set_phone(self, phone_number):
        self.wait_for_overlay()
        phone_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_button))
        self.driver.execute_script("arguments[0].click();", phone_btn)
        time.sleep(1)

        phone_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_input))
        phone_field.clear()
        clean_phone = phone_number.replace(" ", "")
        phone_field.send_keys(clean_phone)
        time.sleep(1)

        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_submit_button))
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

    def set_code(self, code):
        code_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_input))
        code_field.clear()
        code_field.send_keys(code)

        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.code_submit_button))
        self.driver.execute_script("arguments[0].click();", button)

    def add_credit_card(self, card_number, card_code):
        time.sleep(1)
        self.wait_for_overlay()

        payment_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method_button))
        self.driver.execute_script("arguments[0].click();", payment_btn)

        add_card = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_card_button))
        self.driver.execute_script("arguments[0].click();", add_card)

        card_num_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_number_input))
        clean_card = card_number.replace(" ", "")
        card_num_field.send_keys(clean_card)

        card_num_field.click()
        time.sleep(0.5)

        card_code_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_code_input))
        card_code_field.send_keys(card_code)

        self.driver.find_element(By.TAG_NAME, 'body').click()
        time.sleep(0.5)

        submit_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "payment-picker")]//button[contains(@class, "button") and not(contains(@class, "close"))]'))
        )
        self.driver.execute_script("arguments[0].click();", submit_card)

        try:
            close_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.card_close_button))
            self.driver.execute_script("arguments[0].click();", close_btn)
        except:
            pass

    def set_comment(self, message):
        self.wait_for_overlay()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_field))
        self.driver.find_element(*self.message_field).send_keys(message)

    def order_blanket_and_handkerchiefs(self):
        self.wait_for_overlay()
        blanket = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blanket_switch)
        )
        self.driver.execute_script("arguments[0].click();", blanket)

    def order_2_ice_creams(self):
        self.wait_for_overlay()
        for _ in range(2):
            plus_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ice_cream_plus))
            self.driver.execute_script("arguments[0].click();", plus_btn)

    def click_final_order(self):
        self.wait_for_overlay()
        order_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button))
        self.driver.execute_script("arguments[0].click();", order_btn)

    def is_car_search_modal_visible(self):
        modal = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.car_search_modal))
        return modal.is_displayed()

    def get_selected_plan(self):
        selected_plan = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".tcard.active .tcard-title"))
        )
        return selected_plan.text

    def get_registered_phone(self):
        phone_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".np-text"))
        )
        return phone_element.text

    def get_payment_method(self):
        payment_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "pp-value-text"))
        )
        return payment_element.text