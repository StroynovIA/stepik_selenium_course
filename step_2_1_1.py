from selenium import webdriver
from time import sleep


link = "http://suninjuly.github.io/math.html"
# привыкаем к хорошему, там где есть возможность обращаться к контекстному менеджеру - нужно использовать его
with webdriver.Chrome() as browser:
    browser.get(link)

    # думаю типовое решение Вам уже примелькалось, хочу познакомить с мощным методом работы Webdriver непосредственно с javascript страницы
    # для погружения в работу с Selenium Вам и так придется изучать html, CSS и javascript
    # вызываем исполнениие javascript, обратите внимание, что метод document.querySelector очень похож на find_element_by_css_selector
    browser.execute_script("""
    function calc(x){
        return Math.log(Math.abs(12*Math.sin(x)));
    }
    
    document.querySelector('#answer').value = calc(parseInt(document.querySelector('#input_value').textContent));
    selectors = ['#robotCheckbox','#robotsRule','button[type = "submit"]'];
    selectors.forEach(selector => {
        document.querySelector(selector).click();
    })
    """)
    alert = browser.switch_to.alert
    print(alert.text.split(' ')[-1])
    alert.accept()
