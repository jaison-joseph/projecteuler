from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

x_coor = 200
y_coor = 100


print = "https://iu.instructure.com/courses/1834116/assignments/9592030"
chr = webdriver.Chrome()
chr.get("https://www.google.com/")
#ActionChains(chr).click("#submit-button-url.btn.btn-primary.px-4").perform()
a = []
a = chr.find_elements_by_class_name('RNmpXc')
print(len(a))
#chr.execute_script("window.print()")
chr.implicitly_wait(3)
ActionChains(chr).move_by_offset(10,10).perform()