import pandas as pd

df1 = pd.read_csv('tweet_dataset1.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df2 = pd.read_csv('tweet_dataset2.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df = pd.concat([df1,df2], axis=0).reset_index().filter(['tweet'])
df.to_csv('tweets_drepression_dataset_expanded.csv')