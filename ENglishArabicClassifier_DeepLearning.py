import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

filepath_dict = {'Lang': 'MergeFiles.txt'}


#build the datasets
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    label = np.full(1698379, 1)
    label = np.append(label, np.full(20000, 2))
    df['label'] = label
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[1698389])


#Defining a Baseline Model
#split To train and test Sets

df_ = df[(df['source'] == 'Lang')]
sentences = df_['sentence'].values
y = df_['label'].values

sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.2, random_state=1000)
'''
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
'''

classifier = LogisticRegression()
classifier.fit(sentences_train, y_train)
score = classifier.score(sentences_test, y_test)

print("Accuracy:", score)
