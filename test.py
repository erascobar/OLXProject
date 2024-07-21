from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()

driver.get("https://olx.ba/register")

driver.maximize_window()
driver.implicitly_wait(7)

driver.find_element(By.XPATH,"(//div/button)[2]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/div[2]/button").click()

driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password")

name = driver.find_element(By.CSS_SELECTOR,"input[type='text']") #mail
name.send_keys('email')


driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Beenger")

dropdown = Select(driver.find_element(By.XPATH,"//div/select[@class='']"))
dropdown.select_by_index(1)

regija = Select(driver.find_element(By.CSS_SELECTOR, "select[label='Regija']"))
regija.select_by_index(10)
time.sleep(2)

mjesto = Select(driver.find_element(By.XPATH,"//select[@label='Mjesto']"))
mjesto.select_by_index(2)

driver.find_element(By.CSS_SELECTOR,"li[class='']").click()

#driver.find_element(By.XPATH,"(//div/a)[2]").click()

wait = WebDriverWait(driver, 4)
a= wait.until(expected_conditions.presence_of_element_located((By.XPATH,"(//div/a)[2]")))
a.click()




#driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#name.clear()
#time.sleep(500)
