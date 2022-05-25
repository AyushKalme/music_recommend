import pandas as pd

df = pd.read_csv(r"music_recommend\dataset\dataset.csv")
inputs = input("enter name")

if (inputs == 'arijit sighn'):
    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijit = data.dropna()
    print(final_arijit)

elif (inputs == 'lata mangeshkar'):
    data = df.where(df.singer_name  == 'lata mangeshkar')
    singer = data.dropna()
    print(singer)
elif (inputs == 'jubin nautiyal'):
    data = df.where(df.singer_name  == 'jubin nautiyal')
    singer = data.dropna()
    print(singer)
else:
    print("wrong singer")