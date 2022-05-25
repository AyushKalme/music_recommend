import pandas as pd

df = pd.read_csv(r"music_recommend\dataset\dataset.csv")
inputs = input("enter name")
emo = input("enter emotion")

if (inputs == 'arijit sighn' and emo == 'select'):
    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijit = data.dropna()
    print(final_arijit)

elif (inputs == 'lata mangeshkar' and emo == 'select'):
    data = df.where(df.singer_name  == 'lata mangeshkar')
    singer = data.dropna()
    print(singer)
elif (inputs == 'jubin nautiyal' and emo == 'select'):
    data = df.where(df.singer_name  == 'jubin nautiyal')
    singer = data.dropna()
    print(singer)
elif (inputs == 'select' and emo == 'sad'):
    data = df.where(df.emotion == 'sad')
    emotion = data.dropna()
    print(emotion)
elif (inputs == 'select' and emo == 'happy'):
    data = df.where(df.emotion == 'happy')
    emotion = data.dropna()
    print(emotion)
elif (inputs == 'arijit sighn' and emo == 'sad'):
    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    
    data = df.where(df1.emotion == 'sad')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
elif (inputs == 'arijit sighn' and emo == 'happy'):
    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    
    data = df.where(df1.emotion == 'happy')
    final_happy_arigit = data.dropna()
    print(final_happy_arigit)
elif (inputs == 'lata mangeshkar' and emo == 'sad'):
    data = df.where(df.singer_name  == 'lata mangeshkar')
    final_latasad = data.dropna()
    df1 = final_latasad
    
    data = df.where(df1.emotion == 'sad')
    final_sad_lata = data.dropna()
    print(final_sad_lata)
elif (inputs == 'jubin nautiyal' and emo == 'sad'):
    data = df.where(df.singer_name  == 'jubin nautiyal')
    final_jubsad = data.dropna()
    df1 = final_jubsad
    
    data = df.where(df1.emotion == 'sad')
    final_sad_jub = data.dropna()
    print(final_sad_jub)
elif (inputs == 'jubin nautiyal' and emo == 'happy'):
    data = df.where(df.singer_name  == 'jubin nautiyal')
    final_jubhappy = data.dropna()
    df1 = final_jubhappy
    
    data = df.where(df1.emotion == 'happy')
    final_happy_jub = data.dropna()
    print(final_happy_jub)
elif (inputs == 'lata mangeshkar' and emo == 'happy'):
    data = df.where(df.singer_name  == 'lata mangeshkar')
    final_lata = data.dropna()
    df1 = final_lata
    
    data = df.where(df1.emotion == 'happy')
    final_happy_lata = data.dropna()
    print(final_happy_lata)
else:
    print("wrong singer or emotion")
