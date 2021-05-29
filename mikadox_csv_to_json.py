import json
import pandas as pd

# read the csv file
csv_df = pd.read_csv('test.csv')
# drop the dataframe row if ws_request_json has no data
ws_request_json = csv_df[csv_df['ws_request_json'].notna()]
# get just ws_request_json column all data in a new obj
# ws_request_json2 = ws_request_json['ws_request_json']
# # make dataframe to dict
# to_dict = ws_request_json2.to_dict()
#
# data_list = []
# for k, v in to_dict.items():  # k for key, v for value
#     # for str data to dict data
#     temp_data = json.loads(v)
#     # append temp_data in the data_list array
#     data_list.append(temp_data)
# # create datafram from list of dict
# df = pd.DataFrame(data_list)
# # export dataframe to json
# df.to_json('csv_to_json_output.json', orient='records')

# todo: new code
json_str = ws_request_json.to_json(orient='records')
list_dict_data = json.loads(json_str)
data_list = []
for data in list_dict_data:
    ws_request_json = json.loads(data.get('ws_request_json'))
    temp_dict = {'@timestamp': data['@timestamp'],
                 'total_results': data['total_results'],
                 'ws_call': data['ws_call'],
                 'searchType':ws_request_json.get('getArticles').get('searchType'),
                 'searchQuery': ws_request_json.get('getArticles').get('searchQuery'),
                 }

    data_list.append(temp_dict)

# create datafram from list of dict
df = pd.DataFrame(data_list)
# export dataframe to json
df.to_json('csv_to_json_output.json', orient='records')