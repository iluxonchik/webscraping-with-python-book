from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = "C:/phantomjs/bin/phantomjs.exe")
driver.get("http://pythonscraping.com/")
driver.get_screenshot_as_file("pythonscraping.png")