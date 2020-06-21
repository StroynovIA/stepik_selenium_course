import unittest
from time import sleep
from selenium import webdriver


def check_link(link, browser, person):
    browser.get(link)
    for key in person:
        browser.find_element_by_css_selector(f'.form-control.{key}[required]').send_keys(person[key])
    browser.find_element_by_css_selector('button[type = "submit"]').click()
    return browser.find_element_by_tag_name("h1").text

    
class TestAbs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.person = {
                'first' : 'Vasya',
                'second': 'Pupkin',
                'third': 'vasya@yandex.ru'
                }
                
    def test_abs1(self):
        self.assertEqual(check_link('http://suninjuly.github.io/registration1.html', self.browser, self.person), 
        "Congratulations! You have successfully registered!", "Failed")
    
    def test_abs2(self):
        self.assertEqual(check_link('http://suninjuly.github.io/registration2.html', self.browser, self.person), 
        "Congratulations! You have successfully registered!", "Failed")
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        
        
if __name__ == "__main__":
    unittest.main()
