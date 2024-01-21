from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
processDiscoveryURL = "https://www.automationanywhere.com/products/process-discovery"


def explicitWait(element):
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, element)))


def test_Process_Discovery():
    driver.get('https://www.automationanywhere.com/')
    explicitWait("//button[@id='onetrust-accept-btn-handler']")
    driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
    explicitWait("//a[text()='Products']")
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.XPATH, "//a[text()='Products']"))
    actions.perform()
    explicitWait("//a[@href='/products/process-discovery']")
    driver.find_element(By.XPATH, "//a[@href='/products/process-discovery']").click()

    assert driver.current_url == processDiscoveryURL
