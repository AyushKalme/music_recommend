from turtle import shape
from bs4 import BeautifulSoup
import pandas as pd
import emotion



df = pd.read_csv(r'D:\Internship\git\music_recommend\dataset\dataset.csv')
print(df.columns)

# val = df["singer name "].value_counts()
# print(val)

# expression = 'sad'
# emotion.emotions(expression)
print(df)
#     print(type(df))
#         output:<class 'pandas.core.frame.DataFrame'>
#     print(len(df))
#         output:10
#     print(df.shape)
#         output:(10, 7)
#     print(df.info())
    


#     df.drop_duplicates(inplace=True,subset=['song name'])

#     emotion_word=emotion_testing()
#     if emotion_word=='sad':
#         emotion_code=0
#     else:
#         emotion_code=1

#     def get_results(emotion_code):
#       NUM_RECOMMEND=3
#       happy_set=[]
#       sad_set=[]
#       if emotion_code==0:
#           happy_set.append(df[df['kmeans']==0]['song_name'].head(NUM_RECOMMEND))
#           return pd.DataFrame(happy_set).T
#       else:
#           sad_set.append(df[df['kmeans']==1]['song_name'].head(NUM_RECOMMEND))
#           return pd.DataFrame(sad_set).T


#     print(get_results(emotion_code))
#     if emotion_word=='sad':
#         print('emotion detected is SAD')
#     else:
#         print('emotion detected is HAPPY')