import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

def twint_config():
  config = twint.Config()
  config.Pandas = True # use pandas integration
  config.Lang = 'en' # language
  config.Limit = 20 # config max. number of tweets returned (min. 20)
  config.Since = '2022-01-21 00:00:00' # fetch since data
  config.Until = '2022-01-28 00:00:00' # fetch until data
  config.Hide_output = True # hide output of tweets when running
  return config

keywords = pd.read_csv('keywords.csv', encoding='ISO8859', usecols=['0'], squeeze=True).tolist() # get keywords to search
df = pd.DataFrame([], columns=['tweet']) # base dataframe to save data
config = twint_config() # twint configuration 
missed_keywords = [] # list of keywords that return error
n = len(keywords) # total number of keywords
count = 0 # counting of progress
save_ratio = 100 # save dataset in every #save_ratio scrapes

for keyword in keywords:
  try:
    config.Search = keyword # keyword to search
    twint.run.Search(config) # scape tweets with given keyword

    temp = pd.DataFrame(twint.output.panda.Tweets_df['tweet'], columns=['tweet']) # get dataframe of scraped data
    # temp['lang'] = temp['tweet'].map(lambda t: detect_lang(t)) # detect language for each tweet
    # temp = temp[temp['lang'] == 'en'] # filter only english tweets
    # temp = temp.drop(columns=['lang']) # remove language column

    df = pd.concat([df,temp], axis=0) # concatenate new tweets with previous batch
    if((count%save_ratio)==(save_ratio-1)): 
      print("Progress: {:.0%}/100%".format(count/n))
      df.to_csv('dataset' + str(count) + '.csv')
  except: 
    df.to_csv('dataset' + str(count) + '.csv')
    print('Error: the index is %d, and the missed keyword is %s' % (count, keywords[count]))
    missed_keywords.append(keywords[count])
  count +=1
df.to_csv('dataset' + str(count) + '.csv')
pd.DataFrame(missed_keywords).to_csv('missed_keywords.csv')