from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-fullscreen");
options.headless = True
browser = webdriver.Chrome(options=options)
browser.get('http://localhost')
print(browser.title)
browser.quit()