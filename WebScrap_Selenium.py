from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


website = 'https://www.adamchoi.co.uk/overs/detailed'

#Downloads and install the correct version of ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Maximize window and navigate to URL
driver.maximize_window()
driver.get(website)


all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

# select elements in the table
matches = driver.find_elements(By.TAG_NAME, 'tr')

# storage data in lists
date = []
home_team = []
score = []
away_team = []

# looping through the matches list
for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)
# quit driver
driver.quit()

# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=False)
print(df)
