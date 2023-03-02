"""
This module contains the ScrapingTools Class.
"""
from time import sleep
from typing import Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


class ScrapingTools:
    """
    This class contains some handy methods used to scrape any possible website,
    wrapped around the selenium webdriver.
    """
    @staticmethod
    def init_firefox_webdriver(
        url: str,
        excecutable_path: str = "",
        headless: bool = True,
        winsize: tuple = (1920, 1080)
    ) -> webdriver.Firefox:
        """
        Initialize the firefox webdriver and open the browser.
        - Args:
            - url: the url to open in the browser.
            - headless: do operation seeing the actual browser on the scrren
                or not (True for not seeing the bot actually working).
            - winsize: the browser window size, also useful in headless mode
                to understand wich page elements can be seen.
        - Returns:
            - firefox_driver: the webdriver object.
        """
        options = Options()
        options.headless = headless
        if excecutable_path:
            firefox_driver = webdriver.Firefox(
                options=options,
                executable_path=excecutable_path
            )
        else:
            print("Excecutable path not provided, downloading geckodriver...")
            firefox_driver = webdriver.Firefox(
                options=options,
                service=Service(GeckoDriverManager().install())
            )
        firefox_driver.set_window_size(winsize[0], winsize[1])
        firefox_driver.get(url)
        sleep(5)
        return firefox_driver

    @staticmethod
    def click_button(
        driver: webdriver,
        xpath: str,
        wait: int = 10,
        silent: bool = False
    ) -> Union[bool, None]:
        """
        Wraps the click of a button.
        - Args:
            - driver: selenium webdriver.
            - xpath: xpath of the button.
            - wait: how much time to wait for the button to be clickable.
            - silent: if true and the wait is over, the method will just
                return None, otherwise it will raise a selenium webdriver
                exception.
        - Raises:
            - selenium webdriver exception.
        - Returns:
            - True: button click was successful.
            - None: button click was not successful (if silent is true).
        """
        try:
            button = WebDriverWait(
                driver, wait
            ).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            button.click()
            return True
        except (NoSuchElementException, TimeoutError) as exc:
            if not silent:
                raise exc
            return None

    @staticmethod
    def compile_field(
        driver: webdriver,
        xpath: str,
        value: str,
        clear: bool = True
    ) -> None:
        """
        Compile a web field with a value.
        - Args:
            - driver: selenium webdriver.
            - xpath: xptah of the field.
            - value: value to insert into the field.
            - clear: clear the field before inserting the value.
        """
        field = driver.find_element(By.XPATH, xpath)
        if clear:
            field.clear()
        field.send_keys(value)

    @staticmethod
    def get_element_by_xpath(
        driver,
        xpath: str,
        wait: int = 0,
        silent: bool = False
    ) -> Union[WebElement, None]:
        """
        Wraps the return of a webelement.
        - Args:
            - xpath: element xpath.
            - wait: max time to wait for the element to be present.
            - silent: if True and the element's xpaths is not found after
                the wait time, the method will return None, otherwise it will
                raise a selenium webdriver exception.
        - Raises:
            - selenium webdriver exception.
        - Returns:
            - WebElement: Selenium WebDriver WebElement.
            - None: if silent is True and the element's xpaths
                is not found after the wait time.
        """
        try:
            if wait:
                return WebDriverWait(
                    driver, wait
                ).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return driver.find_element(By.XPATH, xpath)
        except (NoSuchElementException, TimeoutException) as exc:
            if not silent:
                raise exc
            return None

    @staticmethod
    def keyboard_insert(
        driver: webdriver,
        string: str = "",
        press_enter: bool = True
    ) -> None:
        """
        Use selenium ActionChains to insert a string into a web field
        usefull for inserting a string into a field that is not visible
        or not intended to be filled by the user, basically simulating
        a keyboard input.
        - Args:
            - driver: selenium webdriver.
            - string: string to insert.
            - press_enter: press the Enter key after inserting the string.
        """
        # pylint: disable=expression-not-assigned
        with ActionChains(driver) as action_chains:
            action_chains.send_keys(string)
            action_chains.send_keys(Keys.ENTER) if press_enter else None
            action_chains.perform()
