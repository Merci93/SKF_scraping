# Description
A web scraping activity to extract the top 200 movies of all time from the IMDb site using the search query `top 500 movies of all time` in [Google Search Engine](https://www.google.com), with Selenium and Chrome webdriver. [Selenium](https://selenium-python.readthedocs.io/) (a web browser automation tool) was selected for this task because of the automation capabilities it offers such as `click()`, `wait`, and `webdriver`.

The script `clicks` searches the keyword, selects the first result and scrolls through each page, gathereing the required data. It terminates at the end of the page and saves the extracted data in a CSV format.

# Installs
1. selenium
2. pandas
3. chrome web driver (version 109.0.5414.75 was used)

> You will need to have chrome webdriver for the version you are running, saved in a directory of your choice, preferabley same directory with the script.
> 1. Go to **Customize and Control Google Chrome** <img width="12" alt="image" src="https://user-images.githubusercontent.com/94759082/211974344-aa321e75-45db-41d6-831d-1abc61234580.png">
> 2. Select **Help** and click **About Google Chrome** to see your chrome version. Doing this might automatically update your chrome to the latest version, hence you will have to download the latest chrome driver.
> [Download Chrome Webdriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0)

# Data
The following data were extracted from the webpage and saved as a CSV file:
1. movie title
2. release year
3. genre
4. run time
5. category
6. rating
7. votes
8. gross
9. director
10. description

>PS: The script was developed for the particular search query: `Top 200 movies of all time` and the IMDb result. Modifications will have to be made for any other search query.
