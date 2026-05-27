import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)

    yield driver
    driver.quit()

def test_card_num_empty(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    inputs = driver.find_elements(by=By.CSS_SELECTOR, value='input[type="text"]')
    assert len(inputs) == 1

def test_card_num_15symbol(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 15)

    num = card_num.get_attribute('value').replace(' ', '')
    assert len(num) == 15

    inputs = driver.find_elements(by=By.CSS_SELECTOR, value='input[type="text"]')
    assert len(inputs) == 1

def test_card_num_16symbol(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    num = card_num.get_attribute('value').replace(' ', '')
    assert len(num) == 16

    inputs = driver.find_elements(by=By.CSS_SELECTOR, value='input[type="text"]')
    assert len(inputs) == 2

def test_card_num_17symbol(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 17)

    num = card_num.get_attribute('value').replace(' ', '')
    assert len(num) == 16

    inputs = driver.find_elements(by=By.CSS_SELECTOR, value='input[type="text"]')
    assert len(inputs) == 2

def test_transaction_commission(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("1234")

    com = driver.find_element(by=By.ID, value='comission')
    assert com.text == "123"

def test_transaction_sum_default(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 1

def test_transaction_sum_not_default(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("1234")

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 1

def test_transaction_sum_empty(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 0

def test_transaction_sum_zero(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("0")

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 0

def test_transaction_sum_negative(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("-1000")

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 0

def test_transaction_sum_on_limit(driver):
    balance = 30000
    reserved = 20000
    driver.get(f'http://localhost:8000/?balance={balance}&reserved={reserved}')

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    spend_amount = balance - reserved
    actual_spend = (spend_amount - (spend_amount - 1) // 11)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys(str(actual_spend))

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 1

def test_transaction_sum_over_limit(driver):
    balance = 30000
    reserved = 20000
    driver.get(f'http://localhost:8000/?balance={balance}&reserved={reserved}')

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    spend_amount = balance - reserved
    actual_spend = (spend_amount - (spend_amount - 1) // 11) + 1

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys(str(actual_spend))

    button = driver.find_elements(by=By.CSS_SELECTOR, value='button')
    assert len(button) == 0

def test_transaction_symbol_limit(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("9" * 7)

    assert transaction_sum.get_attribute('value') == '1000000'

def test_commission_update(driver):
    driver.get("http://localhost:8000/?balance=30000&reserved=20001")

    rubles = driver.find_elements(by=By.CSS_SELECTOR, value='div[class*="g-card_clickable"]')[0]
    rubles.click()

    card_num = driver.find_element(by=By.CSS_SELECTOR, value='input[type=text]')
    card_num.send_keys('0' * 16)

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')
    while len(transaction_sum.get_attribute('value')) != 0:
        transaction_sum.send_keys(Keys.BACKSPACE)
    transaction_sum.send_keys("1234")

    card_num.send_keys(Keys.BACKSPACE)
    card_num.send_keys("1")

    transaction_sum = driver.find_element(by=By.CSS_SELECTOR, value='input[value="1000"]')

    com = driver.find_element(by=By.ID, value='comission')
    actual_com = int(transaction_sum.get_attribute('value')) // 10

    assert com.text == str(actual_com)