from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\rtan0001\\chromedriver.exe")

driver.get("https://ucuat-monashpartner.cs58.force.com/admissions/s/login/")

driver.implicitly_wait(30)

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='74:2;a']").send_keys("rupa.tanneero+77@monash.edu")

driver.find_element_by_xpath("//*[@id='92:2;a']").send_keys("monash@2017")

driver.find_element_by_xpath("//*[@id='centerPanel']/div/div[2]/div/div[4]/div/div[3]/button/span").click()

driver.implicitly_wait(80)

driver.find_element_by_xpath("//*[@id='container']/div[1]/div/button").click()

driver.implicitly_wait(80)


elem1 = driver.find_element_by_xpath("//input[@placeholder='Enter course code or name']")

search_elem = driver.find_element_by_xpath("//*[@id='searchCourse']/div[5]/form/div[2]/div")

actions = ActionChains(driver)

actions.move_to_element(elem1).click()

driver.find_element_by_xpath("//input[@placeholder='Enter course code or name']").send_keys("master")

actions.move_to_element(search_elem).click()






