"""
This module contains all the xpaths used in the project.
"""
from dataclasses import dataclass


@dataclass
class Xpaths:
    """
    This class contains all the xpaths used in the project.
    """
    # Xpaths for the main page
    URL = "https://cercoetrovo.it/"
    ACCEPT_COOKIES = '//*[@id="cookieAccept"]'
    COMUNE_FIELD = '//*[@id="id-luogo"]'
    SEARCH_BUTTON = '/html/body/div[4]/div/main/form/div/div[5]/div/input'
    CONTAINERS = '/html/body/div[4]/div/main/a[{number}]/div[2]/div'
    NEXT_PAGE_BUTTON = '/html/body/div[4]/div/main/span[1]/nav/ul/li[6]/a'

    # Xpaths for the item page
    LOCATION = '/html/body/div[4]/div/main/div[3]/div[1]'
    DATETIME = '/html/body/div[4]/div/main/div[3]/div[2]'
    DESCRIPTION = '/html/body/div[4]/div/main/div[4]/div[1]'
    PRICE = '/html/body/div[4]/div/main/div[4]/div[2]'
    DETAILS = '/html/body/div[4]/div/main/div[5]/div'
    PHONE_NUMBER = '/html/body/div[4]/div/main/div[5]/div/div/a'
    BACK_BUTTON = '/html/body/div[4]/div/main/button'
