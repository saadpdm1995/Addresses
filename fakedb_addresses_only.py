import pandas as pd
import numpy as np
import json
import traceback


# Create dataframe with column headers
df = pd.DataFrame(columns=['camID','address','city','country','lat','long','cap','viz'])

# Open the address file and crete empty lists
# I got the data from https://github.com/EthanRBrown/rrad
file_path = 'insert file path here'
with open(file_path) as f:
    data = json.load(f)
    count = 0
    address1 = []
    city1 = []
    lo = []
    la = []

# for loop to go through all addresses
    for a in data['addresses']:

# try and except to handle errors for when certain fields are empty in the file
        try:
            address1.append(a['address1'])
            city1.append(a['city'])
            la.append(a['coordinates']['lat'])
            lo.append(a['coordinates']['lng'])
            count += 1
        except Exception:
            traceback.print_exc()
            data['addresses'][count]['city'] = 'empty'
            city1.append(data['addresses'][count]['city'])
            la.append(a['coordinates']['lat'])
            lo.append(a['coordinates']['lng'])
            continue

# poulate database with the values from the file
df['city'] = city1
df['address'] = address1
df['lat'] = la
df['long'] = lo
df['country'] = 'USA'

# Add any metadata, in this case i've added capacity
capacity = []
for c in df['cap']:
    c = int(np.random.normal(1000,500))
    if c>10:
        capacity.append(c)
    else:
        capacity.append(10)
df['cap'] = capacity
df['viz'] = (df['cap']/10).astype(int)
df['camID'] = np.arange(len(capacity))

#Create Json for fake database
df.set_index('camID')
df.to_json('campus.json', orient='records', indent=3)

# you will see errors like "KeyError" for missing fields
print(df)
