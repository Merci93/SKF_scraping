# Web_scraping-Goat_Sneakers
A web scraping activity to extract sneakers details from [Goat Sneakers](https://www.goat.com/sneakers) using Selenium with Chrome webdriver. Selenium framework was chossen for this task beacause the webpage is rendered in Javascript, which BeautifulSoup and request fails to get data from the page.

# Installs
1. selenium
2. lxml
3. pandas
4. requests
5. chrome web driver (version 109.0.5414.75 was used)

> You will need to have the chrome webdriver for the version you are running.
> 1. Go to **Customize and Control Google Chrome** <img width="12" alt="image" src="https://user-images.githubusercontent.com/94759082/211974344-aa321e75-45db-41d6-831d-1abc61234580.png">
> 2. Select **Help** and click **ABout Google Chrome** to see your chrome version. Doing this might automatically update your chrome to the latest version, thus you'll have to download the latest driver for the version.
> [Download Chrome Webdriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0)

# Data
The following data is to be extracted from the webpage:
1. year
2. sneaker name
3. price

More updates coming!!!
