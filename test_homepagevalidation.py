# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHomepagevalidation():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homepagevalidation(self):
    self.driver.get("https://buggy.justtestit.org/")
    self.driver.set_window_size(862, 804)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".center-block > .img-fluid")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(1) .card-header").text == "Popular Make"
    assert self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(2) .card-header").text == "Popular Model"
    assert self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(3) .card-header").text == "Overall Rating"
    assert self.driver.title == "Buggy Cars Rating"
  
