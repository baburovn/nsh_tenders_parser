from selenium import webdriver
import time

url = "https://lukoil.ru/Company/Tendersandauctions/Tenders?tab=1"
# указываем путь до хром-драйвера с полным путем до него. ставим двойной обратный слеш: "\\" в пути
driver = webdriver.Chrome(executable_path="C:\\Users\\babur\\PycharmProjects\\pythonProject1\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(2)
    # driver.findElement(By.xpath("//input[@data-bind="value: SearchQuery']")).sendKeys("Сейсм");
    # kkk = driver.find_element_by_id("searchTenderForm").send_keys("сейсм")
    search_form = driver.find_element_by_xpath("//*[@id='searchTenderForm']/div[1]/div[1]/div/div/input").send_keys(
        "скважи")

    time.sleep(2)
    click_button = driver.find_element_by_xpath("//*[@id='searchTenderForm']/div[2]/div/div/div/button[2]").click()

    # yyy = driver.find_element_by_class_name("button")
    print("заполняю поле запроса", search_form)
    # №yyy.click()
    time.sleep(3)
    # print("нажимаю кнопку Искать", click_button)
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
