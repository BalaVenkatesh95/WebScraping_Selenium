from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Define the website to scrape
website = 'https://www.adamchoi.co.uk/overs/detailed'

# Automatically download and install the correct version of ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Maximize the browser window
driver.maximize_window()

# Open the website
driver.get(website)


