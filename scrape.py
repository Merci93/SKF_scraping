# import modules
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Google search
url = 'https://google.com'

# path to chrome driver
driver_path = "path to chrome driver"

# instantiate chrome driver
driver = webdriver.Chrome(service = Service(driver_path))

# second alternative to dwonloading chrome driver
# driver = webdriver.Chrome()

# open url using chrome driver
driver.get(url)

# modify webpage settings: accept terms, change languge to English
accept_google_terms = driver.find_element(By.XPATH, '//*[@id="W0wltc"]/div').click()
switch_to_english = driver.find_element(By.XPATH, '//*[@id="SIvCob"]/a').click()

# Get input box
input_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# input search query and click
search_query = input_box.send_keys('top 200 movies of all time')
click_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()

# select first result on search page
select_result = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3').click()

# list to hold extracted data
df_list = []

# Loop through all pages
while True:
    
    # loop through movies listed on each page and extract data
    for i in range (1, 101):
        try:
            # Get movie details
            title = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/h3/a').text
            year = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/h3/span[2]').text
            cert = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[1]/span[1]').text
            time = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[1]/span[3]').text
            genre = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[1]/span[5]').text
            rating = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/div[1]/div[1]/span[2]').text
            description = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[2]').text
            director = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[3]/a[1]').text
            votes = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[4]/span[2]').text
            gross = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[3]/div['+str(i)+']/div[2]/p[4]/span[5]').text
            
            # append extracted data into list
            df_list.append({'title': title,
                            'release_year': year.replace('(', '').replace(')', ''),
                            'certificate': cert,
                            'run_time': time,
                            'genre': genre,
                            'rating': rating,
                            'gross (USD)': gross,
                            'votes': votes,
                            'director': director,
                            'description': description})
                
        except:
            continue
    
    # Get next page item
    try:
        # get page number
        next_page_url = driver.find_element(By.LINK_TEXT, 'NEXT').get_attribute('href')
        
        # check last page
        if next_page_url[-1] != '#':
            next_page = driver.find_element(By.LINK_TEXT, 'NEXT').click()
        else:
            break
    
    # break at end of page     
    except:
        break

# exit chrome driver
driver.close()

# create a dataframe with extracted data
df = pd.DataFrame(df_list, columns = ['title', 'release_year', 'certificate', 'run_time', 'genre', 'rating', 'gross (USD)',
                                      'votes', 'director', 'description'])
# save dataframe as CSV file
df.to_csv('Top_200_IMDb_movies_of_all_time.csv', index = False)

# display dataframe
df

