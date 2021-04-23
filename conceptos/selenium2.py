# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MiPruebaDirectora(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        configuracion_navegador = Options()
        configuracion_navegador.headless = True
        # 2º Abrir un navegador
        self.driver =webdriver.Firefox(executable_path='../geckodriver', options=configuracion_navegador )


#        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://www.itnow.es/es/Paginas/Home.aspx")
        driver.find_element_by_id("ctl00_SelectorVariaciones1_varCA").click()
        driver.find_element_by_xpath("(//a[contains(text(),'La nostra filosofia')])[2]").click()
        driver.find_element_by_xpath("//span[@id='DeltaPlaceHolderMain']/div[2]/h2").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //span[@id='DeltaPlaceHolderMain']/div[2]/h2 | ]]
        driver.find_element_by_id("content").click()
        driver.find_element_by_xpath("//div[@id='ctl00_PlaceHolderMain_ctl00_ctl03__ControlWrapper_RichHtmlField']/p[2]").click()
        # Warning: assertTextPresent may require manual changes
        self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"Directora")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
