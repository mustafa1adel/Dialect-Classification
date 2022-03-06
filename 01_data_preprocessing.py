import numpy as np
import pickle
import pandas as pd
from helper import clean_text

with open('Datasets/tweets.pkl', 'rb') as f:
    tweets = pickle.load(f)

#using undersampling 
# Store Tunisian records
TN_records = tweets[tweets.dialect == 'TN'].dialect.count()

# Picking the indices of all dialects
dialect_dict = {
    d : tweets.dialect[tweets.dialect == d].index for d in tweets.dialect.unique()
 }

# Out of the indices we picked, randomly select number of dialects records = number of TN dialect records 
for dialect, indices in dialect_dict.items():
    dialect_dict[dialect] = np.random.choice(indices, TN_records)
    dialect_dict[dialect] = np.array(dialect_dict[dialect])

under_sample_indices = np.concatenate(list(dialect_dict.values()))
# Copy under sample dataset  
under_sampled_data = tweets.iloc[under_sample_indices,:]

# check data after sampling 
under_sampled_data.dialect.value_counts().plot(kind='bar')

# clean the tweet column
under_sampled_data['tweet'] = under_sampled_data.tweet.apply(clean_text)
#show the cleaned data
under_sampled_data.head()

#save the sampled data
with open('sampled_data.pkl', 'wb') as file:
    pickle.dump(under_sampled_data, file)