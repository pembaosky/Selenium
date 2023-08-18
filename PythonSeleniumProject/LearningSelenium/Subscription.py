import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import Driver

# ser = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=ser)


def subscription(self):
    driver = Driver.driver()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Subscriptions"))
        )
        element.click()

        create_company_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Add Subscription"))
        )
        create_company_btn.click()
        # time.sleep(2)
    #     driver.find_element(By.ID, "name").send_keys("Testing interactive company")
    #     driver.find_element(By.ID, "description").send_keys("Lorem Lorem Lorem Lorem")
    #     driver.find_element(By.ID, "contact_name").send_keys("my test contact name")
    #     driver.find_element(By.ID, "contact_number").send_keys("0443344556")
    #     driver.find_element(By.ID, "contact_email").send_keys("test@test.com")
    #     driver.find_element(By.ID, "address_line_1").send_keys("testing_address_1")
    #     driver.find_element(By.ID, "address_line_2").send_keys("testing_address_2")
    #
    #     country_drop_down = driver.find_element(By.TAG_NAME, "select")
    #     dd = Select(country_drop_down)
    #     dd.select_by_index(1)
    #     driver.implicitly_wait(5)
    #
    #     state_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(6) > div:nth-child(3) > div:nth-child(2) > select:nth-child(2)")
    #     dd = Select(state_drop_down)
    #     dd.select_by_visible_text("Dummy state 0 on Andorra")
    #
    #     city_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(6) > div:nth-child(3) > div:nth-child(3) > select:nth-child(2)")
    #     dd = Select(city_drop_down)
    #     dd.select_by_index(2)
    #
    #     driver.find_element(By.ID, "postcode").send_keys("44334")
    #     driver.implicitly_wait(5)
    #
    #     save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Company']")
    #     save_btn.click()
    #     driver.implicitly_wait(5)
    #     time.sleep(2)
    #     driver.implicitly_wait(5)
    #     jobvacancy(None)
    #
    except:
        print("here")
        driver.quit()
