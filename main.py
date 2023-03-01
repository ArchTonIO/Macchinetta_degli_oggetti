"""
The bot starting point.
"""
# pylint: disable=expression-not-assigned
import socket
from pathlib import Path
import pandas
from settings.xpaths import Xpaths
from tools.scraping_tools import ScrapingTools
from scrapers.cerco_e_trovo_ws import CercoeTrovoBot


if __name__ == "__main__":
    outdir = Path("OUTPUT/temp")
    outdir.mkdir(parents=True, exist_ok=True)
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
