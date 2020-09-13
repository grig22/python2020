from selenium import webdriver

browser = webdriver.Chrome()
browser.fullscreen_window()
browser.get('http://yandex.ru')
browser.fullscreen_window()