"""
The bot starting point.
"""
import socket
from os import mkdir
from os.path import isdir
import pandas
from settings.xpaths import Xpaths
from tools.scraping_tools import ScrapingTools
from scrapers.cerco_e_trovo_ws import CercoeTrovoBot


if __name__ == "__main__":
    dirmakin = mkdir("OUTPUT") if not isdir("OUTPUT") else None
    subdirmakin = mkdir("OUTPUT/temp") if not isdir("OUTPUT/temp") else None
    del(dirmakin, subdirmakin)
    if "prod" in socket.gethostname():
        print("running on production server")
        driver = ScrapingTools.init_firefox_webdriver(
            url=Xpaths.URL,
            excecutable_path="/usr/local/bin/geckodriver",
            headless=True
        )
    else:
        print("running on local test machine")
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
