from sklearn.pipeline import Pipeline # import pipeline
from sklearn.feature_extraction.text import CountVectorizer # import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer #import tfidfTransformer
from sklearn.naive_bayes import MultinomialNB # import Multinomial Naive bayes
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle 


# laod the data
with open('Datasets/sampled_data.pkl', 'rb') as f:
    under_sampled_data = pickle.load(f)
    
    
# Split data into features and target labels 
features = under_sampled_data['tweet']
target = under_sampled_data['dialect']

# Split the 'features' and 'target' data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    test_size = 0.20,
                                                    random_state = 30)

# # Show the results of the split
# print("Training set has {} samples.".format(X_train.shape[0]))
# print("Testing set has {} samples.".format(X_test.shape[0]))

# modeling a pipeline
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
# train the model
nb.fit(X_train, y_train)
print('accuracy {:.2f}'.format(nb.score(X_test, y_test) * 100))

# save the model
import pickle

file_name = "Models/mnb_model.pkl"
with open(file_name, 'wb') as f:
    pickle.dump(nb, file= f)

