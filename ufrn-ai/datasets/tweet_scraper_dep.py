import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

def twint_config():
  config = twint.Config()
  config.Pandas = True # use pandas integration
  config.Lang = 'en' # language
  config.Limit = 10000 # config max. number of tweets returned (min. 20)
  config.Since = '2020-01-01 00:00:00' # fetch since data
  config.Until = '2022-01-01 00:00:00' # fetch until data
  
  config.Hide_output = True # hide output of tweets when running
  return config

keywords = ['depression','abasement','abjection','blahs','bleakness','bummer','cheerlessness','dejection','desolation','desperation','despondency','discouragement','dispiritedness','distress','dole','dolefulness','dolor','downheartedness','dreariness','dullness','dumps','ennui','gloom','gloominess','heavyheartedness','hopelessness','lowness','melancholia','melancholy','misery','mortification','qualm','sadness','sorrow','trouble','unhappiness','vapors','woefulness','worry','abjectness','blue' 'funk','disconsolation','heaviness of heart','lugubriosity']

config = twint_config() # twint configuration 
df = pd.DataFrame([], columns=['tweet']) # base dataframe to save data

for keyword in keywords:
  try:
    config.Search = keyword # keyword to search
    twint.run.Search(config) # scape tweets with given keyword
    temp = pd.DataFrame(twint.output.panda.Tweets_df['tweet'], columns=['tweet'])
    df = pd.concat([df,temp], axis=0) # concatenate new tweets with previous batch
  except: df.to_csv('security_backup.csv')
df.to_csv('tweet_depression_dataset.csv')