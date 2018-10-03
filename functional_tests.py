from selenium import webdriver

browser_firefox = webdriver.Firefox()
browser_chrome = webdriver.Chrome()

browser_firefox.get("http://localhost:8000")
browser_chrome.get("http://localhost:8000")

assert "Django" in browser_firefox
