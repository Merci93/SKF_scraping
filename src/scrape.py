"""Extracts top 20 IMDb movies"""

import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configuration import URL, SAVE_PATH


class WebCrawler:
    """A class to extract data from IMDb movies webpage"""

    def __init__(self, url: str = None, save_path: str = None) -> None:
        """
        Get parameters

        :param url: IMDb webpage.
        :param save_path: path to save output CSV file.
        """
        self.url = url 
        self.save_path = save_path

    def extract_data(self) -> None:
        """Extract movie data and save as CSV file."""

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options = options)
        driver.get(self.url)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.ipc-title__text")))
        
        html_data = BeautifulSoup(driver.page_source, "html.parser")
        movies = html_data.find_all("li", {"class":"ipc-metadata-list-summary-item"})
        
        movies_list = []
        for movie in movies:
            title = movie.find("h3", {"class":"ipc-title__text"}).text
            year = [item.text for item in movie.find_all("span", {"class":"sc-b85248f1-6"})][0]
            run_time = [item.text for item in movie.find_all("span", {"class":"sc-b85248f1-6"})][1]
            try:
                certification = [item.text for item in movie.find_all("span", {"class":"sc-b85248f1-6"})][2]
            except IndexError:
                certification = "Not rated"
            try:
                stars = movie.find("span", {"class":"ipc-rating-star"}).text
            except AttributeError:
                stars = ""

            movies_list.append({"title": title,
                                "release_year": year,
                                "certificate": certification,
                                "run_time": run_time,
                                "rating": stars})
                        
        driver.close()
        movie_df = pd.DataFrame(movies_list, columns = ["title", "release_year", "certificate", "run_time", "rating"])
        movie_df.to_csv(os.path.join(self.save_path, "Top_IMDb_movies_of_all_time.csv"), index=False)
        print("Data Extraction completed.")

def scrape_imdb(url: str = URL, save_path: str = SAVE_PATH) -> None:
    """Scrape data"""
    crawler = WebCrawler(url, save_path)
    crawler.extract_data()


if __name__ == "__main__":
    scrape_imdb()

