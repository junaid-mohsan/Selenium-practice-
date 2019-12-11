from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get('https://stage.mckinsey.edx.org/')


