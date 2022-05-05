import pandas as pd
import emotion
df = pd.read_csv(r'D:\Internship\git\music_recommend\dataset\dataset.csv')
# # print(df)
# print(len(df.no))


def arijit_sighn ():
    arijit_sighn_list = []
    

    
    for i in range(len(df.no)):
        if 'arijit sighn' == df.singer_name[i]:
            arijit_sighn_list.append(i)

    data = pd.DataFrame()

    for indexes in arijit_sighn_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijit = data.dropna()
    print(final_arijit)

def lata_mangeshkar ():
    lata_mangeshkar_list = []
    
    
    for i in range(len(df.no)):
        if 'lata mangeshkar' == df.singer_name[i]:
            lata_mangeshkar_list.append(i)

    data = pd.DataFrame()

    for indexes in lata_mangeshkar_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name   == 'lata mangeshkar')
    final_lata = data.dropna()
    print(final_lata)

def jubin_nautiyal ():
    jubin_nautiyal_list = []
    jubin_nautiyal_sadlist = []
    
    
    for i in range(len(df.no)):
        if 'jubin nautiyal' == df.singer_name[i]:
            jubin_nautiyal_list.append(i)
    
    data = pd.DataFrame()

    for indexes in jubin_nautiyal_list:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name   == 'jubin nautiyal')
    final_jubin = data.dropna()

    print(final_jubin)



jubin_nautiyal()
arijit_sighn()
lata_mangeshkar()