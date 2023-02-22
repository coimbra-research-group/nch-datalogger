"""
Get html from datalogger.
Code written with assistance of gpt-3
"""

import os
import time
import requests

# TODO need to verify the url to use
ip_address = 'cr1000-datalogger.ucsd.edu/?command=TableDisplay&table=01_Min'

# Make GET request to IP address
response = requests.get(f"http://{ip_address}")

# Filename of html stored locally with timestamp of request
folder = os.path.join("data", "html")
timestamp = time.strftime("%Y%m%d_%H%M")
filename = os.path.join(folder, f'{timestamp}_table.html')

# Check if request was successful
if response.status_code == 200:
    # # Set character encoding of response, may not need this
    # response.encoding = 'windows-1252'

    # Write html content to local file
    with open(filename, 'w') as f:
        # may need to edit the character encoding here
        f.write(response.content.decode('utf-8'))
    print(f'Successfully wrote HTML')
else:
    print(f'Request to {ip_address} failed with '
          f'status code {response.status_code}')