import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

def twint_config():
  config = twint.Config()
  config.Pandas = True # use pandas integration
  config.Lang = 'en' # language
  config.Limit = 100 # config max. number of tweets returned (min. 20)
  config.Since = '2020-01-01 00:00:00' # fetch since data
  config.Until = '2022-01-01 00:00:00' # fetch until data
  config.Search = 'depression' # keyword to search
  config.Hide_output = True # hide output of tweets when running
  return config

df = pd.DataFrame([], columns=['tweet']) # base dataframe to save data
config = twint_config() # twint configuration 
missed_keywords = [] # list of keywords that return error
count = 0 # counting of progress
save_ratio = 100 # save dataset in every #save_ratio scrapes

total_tweets = 10000
n = total_tweets/config.Limit
for i in range(int(n)):
  try:
    twint.run.Search(config) # scape tweets with given keyword
    temp = pd.DataFrame(twint.output.panda.Tweets_df['tweet'], columns=['tweet']) # get dataframe of scraped data

    df = pd.concat([df,temp], axis=0) # concatenate new tweets with previous batch
    if((count%save_ratio)==(save_ratio-1)): 
      print("Progress: {:.0%}/100%".format(count/n))
      df.to_csv('tweet_dataset' + str(count) + '.csv')
  except: 
    df.to_csv('tweet_dataset' + str(count) + '.csv')
    print('Error: the index is %d,' % (count))
  count +=1

df.to_csv('tweet_dataset' + str(count) + '.csv')