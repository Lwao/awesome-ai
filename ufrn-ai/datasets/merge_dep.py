import pandas as pd

df1 = pd.read_csv('dep_tweet1.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df2 = pd.read_csv('dep_tweet2.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df3 = pd.read_csv('dep_tweet3.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df4 = pd.read_csv('dep_tweet4.csv', encoding='ISO8859', usecols=['tweet'], squeeze=True)
df = pd.concat([df1,df2,df3,df4], axis=0).reset_index().filter(['tweet'])
df.drop_duplicates(['tweet'], inplace=True)
df.to_csv('tweets_drepression_dataset_expanded.csv')