#This program utilizes code from Geeks for Geeks: https://www.geeksforgeeks.org/convert-html-table-into-csv-file-in-python/

import re
import pandas as pd
from bs4 import BeautifulSoup
  
# reading Table Display HTML file
with open("Table Display_01.html", "r") as f: 
    soup = BeautifulSoup(f, "html.parser")

# init list and # of rows to retrieve
data = []
num_retrieve = 24

# retrieve last date & time entry to name CSV with
last_date_list = soup.find_all(text=re.compile("20..-..-.."))[-1:]
last_date_str = ''.join(last_date_list)
last_date = last_date_str.replace(":", ".") # colons removed to comply with Windows filename standards

# for getting the header from the HTML file
data_headers = []
data_headers_search = soup.find_all("table")[0].find("tr")
 
for index, header in enumerate(data_headers_search):
    if index%2 == 1: #half the columns in the table are empty without this additional command
        try:
            data_headers.append(header.get_text())
        except:
            continue
 
# for getting the data
data_values_search = soup.find_all("table")[0].find_all("tr")[-num_retrieve:] #retrieves last X number of rows of data
 
for data_row in data_values_search:
    data_values = []
    for index_two, data_val in enumerate(data_row):
        if index_two%2 == 1: #half the columns in the table are empty without this additional command
            try:
                data_values.append(data_val.get_text())
            except:
                continue
    data.append(data_values)
 
# Storing the data into Pandas DataFrame
data_frame = pd.DataFrame(data = data, columns = data_headers)
  
# Converting Pandas DataFrame into CSV file
data_frame.to_csv('Log ' + last_date + '.csv')