from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path="C:/phantomjs/bin/phantomjs.exe")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()