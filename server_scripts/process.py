# =============================================================================
# 
# Translate HTML output from datalogger into CSV for use in plot.py using BS4.
# Code prepared by Benjamin Tarver. Last updated Nov 20, 2023.
# 
# =============================================================================


from bs4 import BeautifulSoup
import glob
import os
import pandas as pd
import time
from sqlalchemy import create_engine

# Begin code borrowed from https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder

# Gets latest file from directory in which new measurment records are stored
list_of_files = glob.glob('/home/ladmin/datalogger/data/html/*')
latest_file = max(list_of_files, key=os.path.getctime)

# End borrowed code

# Converts HTML file into BS4 output
with open(latest_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Begin borrowed code from https://www.geeksforgeeks.org/convert-html-table-into-csv-file-in-python/

# Initialize empty data array
data = []
  
# Get header content from BS4 output
list_header = []
header = soup.find_all("table")[0].find("tr")
 
# Get header text
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        raise Exception("There was an error retrieving the column headers.")
    
# Get data values from BS4 output
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            raise Exception("There was an error retrieving the data.")
    data.append(sub_data)

# Store the data into Pandas DataFrame 
df = pd.DataFrame(data = data, columns = list_header)
df.rename(columns={'WS_WVc(1)': 'WS_WVc_1', 'WS_WVc(2)': 'WS_WVc_2', 'TimeStamp': 'time'}, inplace=True)

# End borrowed code

# Remove milliseconds from time column values
df['time'] = df['time'].str[:-2]

# Drop blank columns
df = df.drop(df.columns[[0]], axis=1)

# Save dataframe to MySQL table in server database
engine = create_engine(r'mysql+pymysql://root:db4datalogger!1@localhost/datalogger')
df.to_sql('Seventh_CR1000_Data', con=engine, if_exists='append', index=False)
print('Successfully wrote SQL, in theory')

# Remove HTML file source ()
# Filename of html stored locally with timestamp of request
try:
        os.remove(latest_file)
except OSError as e:
        print('Error deleting HTML file.');

