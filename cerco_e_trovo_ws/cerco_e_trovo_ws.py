"""
This module contains the bot class that holds the high level
functions to perform the scraping on 'cerco e trovo' website.
This module explicitly use firefox webdriver.
"""
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from xpaths import Xpaths
from scraping_tools import ScrapingTools
from progress_indicators import print_progress_bar


class CercoeTrovoBot:
    """
    The cerco e trovo scraping bot class
    """
    @staticmethod
    def perform_homepage_interactions(
        firefox_driver: webdriver.Firefox,
        search_area: str
    ) -> None:
        """
        Perform the homepage interactions.
        - Args:
            - driver: the webdriver object.
            - search_area: the area to search for.
        """
        ScrapingTools.click_button(
            driver=firefox_driver,
            xpath=Xpaths.ACCEPT_COOKIES
        )
        ScrapingTools.compile_field(
            driver=firefox_driver,
            xpath=Xpaths.COMUNE_FIELD,
            value=search_area
        )
        ScrapingTools.click_button(
            driver=firefox_driver,
            xpath=Xpaths.SEARCH_BUTTON
        )

    @staticmethod
    def cycle_trought_pages(
        driver: webdriver.Firefox,
        start_page: int,
        end_page: int
    ) -> dict:
        """
        A generator function that cycle trought the pages
        of the website.
        This method uses two underlying private methods:
            - __cycle_trought_items
            - __fetch_item_data
        - Args:
            - start_page: the page to start from.
            - end_page: the page to end to.
        - Yields:
            - data (dict): the data scraped from a single item on the page.
            - page (int): the page number.
        """
        print("> DOWNLOADING DATA <\n")
        for page in range(start_page, end_page):
            print_progress_bar(iteration=page, total=end_page)
            data = CercoeTrovoBot.__cycle_trought_items(driver)
            if page in (1, 113):
                next_page_button_xpath = Xpaths.NEXT_PAGE_BUTTON_1
            elif 1 < page < 113:
                next_page_button_xpath = Xpaths.NEXT_PAGE_BUTTON_2
            else:
                next_page_button_xpath = Xpaths.LAST_PAGE
            ScrapingTools.click_button(
                driver=driver,
                xpath=next_page_button_xpath,
                wait=2
            )
            sleep(2)
            yield data, page

    @staticmethod
    def __cycle_trought_items(
        driver: webdriver.Firefox,
        start_item: int = 1,
        stop_item: int = 41
    ) -> dict:
        """
        Private method to cycle trought the items on the page.
        - Args:
            - driver: the webdriver object.
            - start_item: the item to start from.
            - stop_item: the item to end to. (usually 41 for this website)
        - Returns:
            - data (dict): the data scraped from a single item on the page.
        """
        data_dicts = []
        for i in range(start_item, stop_item):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)"
            )
            try:
                ScrapingTools.click_button(
                    driver=driver,
                    xpath=Xpaths.CONTAINERS.format(number=i),
                    wait=2
                )
            except TimeoutException:
                ScrapingTools.click_button(
                    driver=driver,
                    xpath=Xpaths.SMALL_CONTAINERS.format(number=i),
                    wait=2
                )
            data = CercoeTrovoBot.__fetch_item_data(driver)
            ScrapingTools.click_button(
                driver=driver,
                xpath=Xpaths.BACK_BUTTON,
                silent=True
            )
            data_dicts.append(data)
        page_dict = {}
        for data_dict in data_dicts:
            for key, value in data_dict.items():
                page_dict.setdefault(key, []).extend(value)
        return page_dict

    @staticmethod
    def __fetch_item_data(driver: webdriver.Firefox) -> dict:
        """
        Private method to fetch the item data.
        - Args:
            - driver: the webdriver object.
        - Returns:
            - data_dict (dict): the data scraped from
                a single item on the page.
        """
        items_xpaths = [
            Xpaths.LOCATION,
            Xpaths.DATETIME,
            Xpaths.DESCRIPTION,
            Xpaths.PRICE,
            Xpaths.DETAILS,
            Xpaths.PHONE_NUMBER
        ]
        data_dict = {
            "LOCATION": [],
            "DATETIME": [],
            "DESCRIPTION": [],
            "PRICE": [],
            "DETAILS": [],
            "PHONE_NUMBER": []
        }
        xpaths_counter = 0
        for item in data_dict.items():
            try:
                item[1].append(
                    ScrapingTools.get_element_by_xpath(
                        driver=driver,
                        xpath=items_xpaths[xpaths_counter],
                        silent=True
                    ).text.strip()
                )
            except AttributeError:
                item[1].append("not found")
            xpaths_counter += 1
        return data_dict
