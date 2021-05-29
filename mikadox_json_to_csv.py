import json

import pandas as pd

# read the json file
with open('csv_to_json_output.json', 'rb') as json_file:
    # make json data to dict data by json.loads() method
    dict_data = json.loads(json_file.read())

# store filtered data dict-object in this list
data_list = []
# using 'for loop' for get each single json data object and get the filetered key values
for data in dict_data:
    # temp dict object
    temp_dict = {
        "@timestamp": data['@timestamp'],
        "total_results": data['total_results'],
        "ws_call": data['ws_call'],
        "searchType": data['searchType'],
        "searchQuery": data['searchQuery']
    }
    # append the dict object in the list
    data_list.append(temp_dict)

# pass the list data in the datafram
df = pd.DataFrame(data_list)
# create desired output csv file from df(dataframe) to csv file.
df.to_csv('output.csv', index=False)
