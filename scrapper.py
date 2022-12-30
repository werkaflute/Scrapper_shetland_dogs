from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url_driver, website_url):
        self.driver = webdriver.Chrome(url_driver)
        self.driver.get(website_url)

    def start_scrapping(self):
        speed = 30
        times_scrolling = 1
        self.scroll_down_page(speed)
        self.accept_cookie_button()
        for i in range(times_scrolling):
            self.scroll_down_page(30)

    def scroll_down_page(self, speed):
        current_scroll_position, new_height = 0, 1
        while current_scroll_position <= new_height and current_scroll_position < 6000:
            current_scroll_position += speed
            self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
            new_height = self.driver.execute_script("return document.body.scrollHeight")

    def accept_cookie_button(self):
        cookie_button = self.driver.find_element(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/"
                                                           "div[1]/form[2]/div/div/button/span")
        if cookie_button is not None:
            cookie_button.click()

    def get_div_with_img(self):
        div_elements = []
        response = self.driver.page_source
        soup = BeautifulSoup(response, "html.parser")
        for img in soup.find_all('div', {'class': 'isv-r PNCib MSM1fd BUooTd'}):
            div_elements.append(img)
        return div_elements
