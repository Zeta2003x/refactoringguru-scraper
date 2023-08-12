import chrome_driver_setup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes



def trabajar_patron(url_patron:str):
    driver.switch_to.new_window(WindowTypes.TAB)
    driver.get(url_patron)
    print(driver.find_element(By.XPATH, "/html/body/div/main/div/div/article/div[3]/p").text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


driver = chrome_driver_setup.create_chrome_driver()
original_window = "https://refactoring.guru/es/design-patterns/catalog"
driver.get(original_window)
patterns = driver.find_elements(By.CSS_SELECTOR, ".pattern-card")
list(map((lambda pattern: trabajar_patron(pattern.get_attribute('href'))), patterns))
