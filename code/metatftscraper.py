from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
import csv
from bs4 import BeautifulSoup

URL = "https://www.metatft.com/units"

# Set up Selenium WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Fetch the page
print("Fetching the page...")
driver.get(URL)

# Wait for the page to load
driver.implicitly_wait(20)

# Get the page source
page_content = driver.page_source
driver.quit()

soup = BeautifulSoup(page_content, 'html.parser')

# Find all rows
rows = soup.find_all('tr', role="row")
print(f"Number of rows found: {len(rows)}")

data = []
for row in rows:
    unit = row.find('a', class_='StatLink')
    ave_place = row.find('div', class_='TablePlacement TablePlacementRow')
    win_rate = row.find('div', class_='TableNum TableNumRow')
    frequency = row.find('div', class_='TableNumRight TableNumRow')
    
    # Check if all elements are found
    if unit and ave_place and win_rate and frequency:
        unit = unit.text.strip()
        ave_place = ave_place.text.strip()
        win_rate = win_rate.text.strip()
        frequency = frequency.text.strip()
        print(unit, ave_place, win_rate, frequency)
        data.append([unit, ave_place, win_rate, frequency])
    else:
        print("Some elements were not found in this row.")
    
with open('data/unitperformancedata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Unit", "Average Place", "Win Rate", "Frequency"])
    writer.writerows(data)