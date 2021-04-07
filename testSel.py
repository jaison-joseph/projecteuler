from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
btnId = '#submit-button-url.btn.btn-primary.px-4'
printThis = "https://canvas.iu.edu/lms-prd/gateway"
driver.get("https://pdfcrowd.com/")
element = driver.find_element_by_id("submit-button-url") 
  
# create action chain object 
action = ActionChains(driver) 
  
# click the item 
action.click(on_element = element) 
#driver.implicitly_wait(4)
#driver.findElementById(btnId).click()
#driver.executeScript("print()")
#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('p').key_up(Keys.CONTROL).send_keys("s").perform()
#driver.save_screenshot(str(133)+".pdf")