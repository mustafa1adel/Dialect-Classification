import pandas as pd
from requests import post
import json
import pickle

data = pd.read_csv("Datasets/dialect_dataset.csv")
# print(data.info())

data['id'] = data.id.astype(str)



url = "https://recruitment.aimtechnologies.co/ai-tasks"
text = pd.DataFrame()

for i in range(0, data.shape[0], 1000):
    
    print(f"Number of remaining rows is {data.shape[0] - i}") # FOR DEBUGGING
    response = post(url,
                    data= json.dumps(data.id[i: i+1000].values.tolist()))
    
    response = json.loads(response.content.decode('utf-8'))
    d = pd.DataFrame(list(response.items()),
                     columns = ['id', 'tweet'])
    text = text.append(d,
                       ignore_index=True)


# merge the retrieved data and tweets.    
tweets = pd.merge(tweets, df, on ='id', how='right')
    
# save df tweets  
fname = 'Datasets/tweets.pkl'
with open(fname, 'wb') as file:
    pickle.dump(tweets, file)
