import time
import Subscription
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
# import Driver

ser = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser)
# driver = Driver.driver()


def login_by_id(self):

    driver.get("https://cvd.osky.dev/auth/login")

    driver.maximize_window()
    print("Title: " + driver.title)
    # print("Driver: " + driver.current_url)
    time.sleep(3)
    driver.implicitly_wait(15)
    driver.find_element(By.ID, "email").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("password")
    login_btn = driver.find_element(By.TAG_NAME, "button")
    login_btn.click()
    time.sleep(3)
    companies(self)



def companies(self):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Companies"))
        )
        element.click()

        create_company_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Create a new company"))
        )
        create_company_btn.click()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Testing interactive company")
        driver.find_element(By.ID, "description").send_keys("Lorem Lorem Lorem Lorem")
        driver.find_element(By.ID, "contact_name").send_keys("my test contact name")
        driver.find_element(By.ID, "contact_number").send_keys("0443344556")
        driver.find_element(By.ID, "contact_email").send_keys("test@test.com")
        driver.find_element(By.ID, "address_line_1").send_keys("testing_address_1")
        driver.find_element(By.ID, "address_line_2").send_keys("testing_address_2")

        country_drop_down = driver.find_element(By.TAG_NAME, "select")
        dd = Select(country_drop_down)
        dd.select_by_index(1)
        driver.implicitly_wait(5)

        state_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(6) > div:nth-child(3) > div:nth-child(2) > select:nth-child(2)")
        dd = Select(state_drop_down)
        dd.select_by_visible_text("Dummy state 0 on Andorra")

        city_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(6) > div:nth-child(3) > div:nth-child(3) > select:nth-child(2)")
        dd = Select(city_drop_down)
        dd.select_by_index(2)

        driver.find_element(By.ID, "postcode").send_keys("44334")
        driver.implicitly_wait(5)

        save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Company']")
        save_btn.click()
        driver.implicitly_wait(5)
        time.sleep(2)
        driver.implicitly_wait(5)
        jobvacancy(self)

    except:
        print("here")
        driver.quit()


def jobvacancy(self):
    print("hi")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Job Vacancies"))
        )
        element.click()

        create_vacancy_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Create a new vacancy / opening"))
        )
        create_vacancy_btn.click()
        time.sleep(2)
        driver.find_element(By.ID, "title").send_keys("abc vacancy")
        driver.find_element(By.ID, "description").send_keys("Lorem Lorem Lorem Lorem")
        driver.implicitly_wait(10)

        company_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(company_drop_down)
        dd.select_by_index(0)           #Company selection from drop down
        driver.implicitly_wait(10)

        industry_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(industry_drop_down)
        dd.select_by_index(0)
        driver.implicitly_wait(10)
        print("here")

        work_type_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(work_type_drop_down)
        dd.select_by_index(2)
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "salary_min").send_keys("25")
        driver.find_element(By.ID, "salary_max").send_keys("40")

        sal_type_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(sal_type_drop_down)
        dd.select_by_index(1)
        driver.implicitly_wait(5)

        currency_type_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(currency_type_drop_down)
        dd.select_by_index(4)
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "contact_name").send_keys("my test contact name")
        driver.find_element(By.ID, "contact_number").send_keys("0443344556")
        driver.find_element(By.ID, "contact_email").send_keys("test@test.com")
        driver.find_element(By.ID, "address_line_1").send_keys("testing_address_1")
        driver.find_element(By.ID, "address_line_2").send_keys("testing_address_2")

        country_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(11) > div:nth-child(3) > div:nth-child(1) > select:nth-child(2)")
        dd = Select(country_drop_down)
        dd.select_by_index(1)
        driver.implicitly_wait(5)

        state_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(11) > div:nth-child(3) > div:nth-child(2) > select:nth-child(2)")
        dd = Select(state_drop_down)
        dd.select_by_visible_text("Dummy state 0 on Andorra")

        city_drop_down = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(11) > div:nth-child(3) > div:nth-child(3) > select:nth-child(2)")
        dd = Select(city_drop_down)
        dd.select_by_index(2)

        driver.find_element(By.ID, "postcode").send_keys("44334")
        driver.implicitly_wait(5)

        save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Vacancy']")
        print("Success")
        save_btn.click()
        time.sleep(2)
        driver.implicitly_wait(5)
        subscription(self)


    except:
        print("job exit")
        driver.quit()


def subscription(self):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Subscriptions"))
        )
        element.click()

        create_company_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Add Subscription"))
        )
        create_company_btn.click()
        driver.implicitly_wait(5)

        driver.find_element(By.ID, "title").send_keys("My New Automatic Subscription ")
        driver.find_element(By.ID, "description").send_keys("lorem lorem lipsum dolor")

        start_date = driver.find_element(By.XPATH, "//input[@id='date_start']")
        start_date.click()

        alldates = driver.find_elements(By.XPATH, "//body[1]/div[1]/form[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/button[2]")

        for date_element in alldates:
            date = date_element.text
            print(date)
            if date == "01":
                date_element.click()
                break

        end_date = driver.find_element(By.XPATH, "//input[@id='date_end']")
        end_date.click()
        alldates = driver.find_elements(By.XPATH,
                                        "//body[1]/div[1]/form[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/button[3]")

        for date_element in alldates:
            date = date_element.text
            print(date)
            if date == "02":
                date_element.click()
                break

        type_drop_down = driver.find_element(By.TAG_NAME,
                                              "select")
        dd = Select(type_drop_down)
        dd.select_by_visible_text("Premium")

        save_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Save Subscription']")
        print("Success")
        save_btn.click()


    except:
        print("from subscription")
        driver.quit()


login_by_id(None)
time.sleep(20)