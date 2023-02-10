"""
The bot starting point
"""
# pylint: disable=import-error
from time import sleep
import pandas
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException
from config.xpaths import Xpaths
from scraping_tools import ScrapingTools
from utils.progress_indicators import print_progress_bar

if __name__ == "__main__":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options,
        service=Service(GeckoDriverManager().install())
    )
    driver.set_window_size(1920, 1080)
    driver.get(Xpaths.URL)
    sleep(5)
    ScrapingTools.click_button(driver=driver, xpath=Xpaths.ACCEPT_COOKIES)
    ScrapingTools.compile_field(
        driver=driver,
        xpath=Xpaths.COMUNE_FIELD,
        value="Perugia"
    )
    ScrapingTools.click_button(driver=driver, xpath=Xpaths.SEARCH_BUTTON)
    data_dict = {
        "LOCATION": [],
        "DATETIME": [],
        "DESCRIPTION": [],
        "PRICE": [],
        "DETAILS": [],
        "PHONE_NUMBER": []
    }
    item_xpaths = [
        Xpaths.LOCATION,
        Xpaths.DATETIME,
        Xpaths.DESCRIPTION,
        Xpaths.PRICE,
        Xpaths.DETAILS,
        Xpaths.PHONE_NUMBER
    ]
    print("DOWNLOADING DATA")
    for i in range(1, 30):
        print_progress_bar(iteration=i, total=30)
        try:
            ScrapingTools.click_button(
                driver=driver,
                xpath=Xpaths.CONTAINERS.format(number=i),
                wait=2
            )
        except TimeoutException:
            continue
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        XPATHS_COUNTER = 0
        for key, value in data_dict.items():
            try:
                value.append(
                    ScrapingTools.get_element_by_xpath(
                        driver=driver,
                        xpath=item_xpaths[XPATHS_COUNTER],
                        silent=True
                    ).text.strip()
                )
            except AttributeError:
                value.append("not found")
            XPATHS_COUNTER += 1
        ScrapingTools.click_button(
            driver=driver,
            xpath=Xpaths.BACK_BUTTON,
            silent=True
        )
    df = pandas.DataFrame(data_dict)
    df.to_csv("data.csv", index=False)
