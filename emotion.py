import pandas as pd

df = pd.read_csv(r'D:\Internship\git\music_recommend\dataset\dataset.csv')

def sad():
    sad_list = []
    
    
    for i in range(len(df.no)):
        if 'sad' == df.emotion[i]:
            sad_list.append(i)

    data = pd.DataFrame()

    for indexes in sad_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.emotion == 'sad')
    final_sad = data.dropna()
    print(final_sad)

    
def happy():
    happy_list = []
    
    
    for k in range(len(df.no)):
        if 'happy' == df.emotion[k]:
            happy_list.append(k)

    data = pd.DataFrame()

    for indexes in happy_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat([data,data_new])

    

    data = df.where(df.emotion == 'happy')
    final_happy = data.dropna()
    print(final_happy)

def emotions(expression):
    if expression == 'happy':
        print("you selected happy songs\n\n\n")
        happy()
    elif expression == 'sad':
        print("you selected sad songs\n\n\n")
        sad()
    else:
        print(df)
