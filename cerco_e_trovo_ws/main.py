"""
The bot starting point.
"""
from os import mkdir
from os.path import isdir
import pandas
from xpaths import Xpaths
from scraping_tools import ScrapingTools
from cerco_e_trovo_ws import CercoeTrovoBot


if __name__ == "__main__":
    dirmakin = mkdir("OUTPUT") if not isdir("OUTPUT") else None
    subdirmakin = mkdir("OUTPUT/temp") if not isdir("OUTPUT/temp") else None
    del(dirmakin, subdirmakin)
    driver = ScrapingTools.init_firefox_webdriver(
        url=Xpaths.URL,
        headless=False
    )
    CercoeTrovoBot.perform_homepage_interactions(
        firefox_driver=driver,
        search_area="Perugia"
    )
    dfs = []
    for data, page in CercoeTrovoBot.cycle_trought_pages(
        driver=driver,
        start_page=1,
        end_page=116
    ):
        df = pandas.DataFrame(data)
        df.to_csv(f"OUTPUT/temp/cerco_e_trovo_page_{page}.csv", index=False)
        dfs.append(df)
    final_df = pandas.concat(dfs)
    final_df.to_csv("OUTPUT/cerco_e_trovo.csv", index=False)
