# Description
A web scraping activity to extract the top 200 movies of all time from the IMDb site using the search query `top 500 movies of all time` in [Google Search Engine](https://www.google.com) using Selenium with Chrome webdriver. [Selenium](https://selenium-python.readthedocs.io/) (a web browser automation tool) was selected for this task because of the automation capabilities it offers as compared to BeautifulSoup.

# Installs
1. selenium
2. lxml
3. pandas
4. chrome web driver (version 109.0.5414.75 was used)

> You will need to have chrome webdriver for the version you are running, saved in a directory of your choice, preferabley same directory with the script.
> 1. Go to **Customize and Control Google Chrome** <img width="12" alt="image" src="https://user-images.githubusercontent.com/94759082/211974344-aa321e75-45db-41d6-831d-1abc61234580.png">
> 2. Select **Help** and click **ABout Google Chrome** to see your chrome version. Doing this might automatically update your chrome to the latest version, thus you'll have to download the latest driver for the version.
> [Download Chrome Webdriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0)

# Data
The following data were extracted from the webpage:
1. movie name
2. release year
3. genre
4. run time
5. category
6. rating
7. metascore
8. director
9. stars/actors
10. votes
11. gross
12. description

More updates coming!!!
