#!/usr/bin/env python
# coding: utf-8

# In[22]:


# connect python with webbrowser-chrome
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# import pyautogui as pag
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
import pandas as pd





s=Service('chromedriver.exe')
browser = webdriver.Chrome()
url = "https://linkedin.com/jobs"   
browser.get(url)
sleep(5)


# In[ ]:


import pandas as pd

# Replace 'your_file.csv' with the actual name of your CSV file
file_path = 'Phase2_LinkedInOutreach.csv'

# Replace 'column_name' with the name of the column you want to read
column_index = 1

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Extract the specified column and store it as a list
#urls = df.iloc[:, column_index].tolist()

#for i in range(1,10):
#    print(urls[i])


# In[ ]:


###def extract_job_description(url):
   # browser.get(url)
    # Modify this line to locate the element containing the job description on the webpage
  #  job_description_element = browser.find_element(By.XPATH, 'your_css_selector')
 #   job_description = job_description_element.text
#    return job_description

#for link in urls:
    # Navigate to the link
   # browser.get(link.strip())

    # Wait for 1 minute
  #  time.sleep(60)

    # Replace 'your_xpath' with the XPath of the element you want to extract text from
 #   element_xpath = 'your_xpath'

    #try:
       # Find the element and extract text
  #      element = driver.find_element_by_xpath(element_xpath)
 #       extracted_text = element.text

      # Print or store the extracted text as needed
#       print(extracted_text)
#
#    except Exception as e:
#        print(f"Error extracting text from {link}: {e}")


# In[ ]:


jd_list = []
hiring_team = []
# Function to extract job description from a webpage
def extract_job_description(url):
    browser.get(url)
    # Modify this line to locate the element containing the job description on the webpage
    element = browser.find_element_by_class_name("ph5")
#     try:
#         # Replace 'your_element_selector' with the appropriate selector for the element you're interested in
#         hr = browser.find_element_by_css_selector('your_element_selector')

#         # Check if the 'your_class_name' class exists in the element's classes
#         if 'your_class_name' in element.get_attribute('class'):
#             # If the class exists, extract and print the element's text
#             hiring_team.append(hr.text)
#             print(f"Element text: {element_text}")
#         else:
#             # If the class doesn't exist, print a message
#             hiring_team.append("nil")
#             print("Class not found for the element.")

#     except NoSuchElementException:
#         # Handle the case where the element is not found on the page
#         hiring_team.append("nil")
#         print("Element not found on the page.")
    
    xpath = element.get_attribute("xpath")

    job_description_element = browser.find_element(By.XPATH,xpath)
    job_description = job_description_element.text
    return job_description #, hiring_team

try:
    # Iterate through each link
    for link in urls:
        link = link.strip()  # Remove leading/trailing whitespaces
        job_description = extract_job_description(link)
        jd_list.append(job_description)

        # Sleep for 1 minute (60 seconds)
        time.sleep(60)

except Exception as e:
    jd_list.append("Error")
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver
    browser.quit()


#Print the resulting job descriptions
for i, jd in enumerate(jd_list, start=1):
  print(f"Job Description {i}:\n{jd}")

# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[5]/section[2]/div/div[1]/div/div/a
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[5]/section[3]/div/div[1]/div/div/a
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[7]/section[2]/div/div[1]/div/div/a
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[7]/section[1]
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[5]/section[1]
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[5]/section[1]
# /html/body/div[5]/div[3]/div[2]/div/div/main/div/div[1]/div/div[5]/section[1]

