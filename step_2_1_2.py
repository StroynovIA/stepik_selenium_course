from selenium import webdriver
from time import sleep


link = "http://suninjuly.github.io/registration1.html"
# привыкаем к хорошему, там где есть возможность обращаться к контекстному менеджеру - нужно использовать его
with webdriver.Chrome() as browser:
    browser.get(link)

    # думаю типовое решение Вам уже примелькалось, хочу познакомить с мощным методом работы Webdriver непосредственно с javascript страницы
    # для погружения в работу с Selenium Вам и так придется изучать html, CSS и javascript
    # вызываем исполнениие javascript, обратите внимание, что метод document.querySelector очень похож на find_element_by_css_selector
    browser.execute_script("""
    var Dude = {
        'first name' : 'Vasya',
        'last name': 'Pupkin',
        'email': 'vasya@yandex.ru'
    }
    Object.keys(Dude).forEach(key => {
        document.querySelector(`input[placeholder="Input your ${key}"]`).value = Dude[key];
    })
    document.querySelector('button[type = "submit"]').click();
    """)

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(5)
    
# Пояснение к отлову ошибки:
# так как мы работали через javascript то и ошибка будет транслирована из его среды, если определенного элемента не будет, 
# то будет ошибка типа "нельзя вызвать свойство value у объекта null", суть та же - по указанному селектору нет ни одного элемента
