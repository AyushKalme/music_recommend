import pandas as pd
df = pd.read_csv(r'dataset\dataset.csv')

def arijit_sighn_sad ():
    arijit_sighn_sadlist = []
    


    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    
    data = df.where(df1.emotion == 'sad')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
    # print(arigitsad_list)


def arijit_sighn_happy ():
    arijit_sighn_happylist = []
    

    
    for i in range(len(df.no)):
        if 'arijit sighn' == df.singer_name[i]:
            arijit_sighn_happylist.append(i)

    data = pd.DataFrame()

    for indexes in arijit_sighn_happylist:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'arijit sighn')
    final_arijithappy = data.dropna()
    df1 = final_arijithappy
    arigithappy_list = []
    
    
    for i in range(len(arigithappy_list)):
        if 'happy' == df1.emotion[i]:
            arigithappy_list.append(i)

    data = pd.DataFrame()

    for indexes in arigithappy_list:
        data = data.append(df1.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df1.emotion == 'happy')
    final_happy_arigit = data.dropna()
    print(final_happy_arigit)
    # print(arigithappy_list)



def lata_sad ():
    lata_sadlist = []
    

    
    for i in range(len(df.no)):
        if 'lata mangeshkar' == df.singer_name[i]:
            lata_sadlist.append(i)

    data = pd.DataFrame()

    for indexes in lata_sadlist:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'lata mangeshkar')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    arigitsad_list = []
    
    
    for i in range(len(arigitsad_list)):
        if 'sad' == df1.emotion[i]:
            arigitsad_list.append(i)

    data = pd.DataFrame()

    for indexes in arigitsad_list:
        data = data.append(df1.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df1.emotion == 'sad')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
    print(arigitsad_list)


def lata_happy ():
    lata_sadlist = []
    

    
    for i in range(len(df.no)):
        if 'lata mangeshkar' == df.singer_name[i]:
            lata_sadlist.append(i)

    data = pd.DataFrame()

    for indexes in lata_sadlist:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'lata mangeshkar')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    arigitsad_list = []
    
    
    for i in range(len(arigitsad_list)):
        if 'happy' == df1.emotion[i]:
            arigitsad_list.append(i)

    data = pd.DataFrame()

    for indexes in arigitsad_list:
        data = data.append(df1.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df1.emotion == 'happy')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
    # print(arigitsad_list)


def jubin_sad ():
    lata_sadlist = []
    

    
    for i in range(len(df.no)):
        if 'jubin nautiyal' == df.singer_name[i]:
            lata_sadlist.append(i)

    data = pd.DataFrame()

    for indexes in lata_sadlist:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'jubin nautiyal')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    arigitsad_list = []
    
    
    for i in range(len(arigitsad_list)):
        if 'sad' == df1.emotion[i]:
            arigitsad_list.append(i)

    data = pd.DataFrame()

    for indexes in arigitsad_list:
        data = data.append(df1.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df1.emotion == 'sad')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
    # print(arigitsad_list)


def jubin_happy ():
    lata_sadlist = []
    

    
    for i in range(len(df.no)):
        if 'jubin nautiyal' == df.singer_name[i]:
            lata_sadlist.append(i)

    data = pd.DataFrame()

    for indexes in lata_sadlist:
        data = data.append(df.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df.singer_name  == 'jubin nautiyal')
    final_arijitsad = data.dropna()
    df1 = final_arijitsad
    arigitsad_list = []
    
    
    for i in range(len(arigitsad_list)):
        if 'happy' == df1.emotion[i]:
            arigitsad_list.append(i)

    data = pd.DataFrame()

    for indexes in arigitsad_list:
        data = data.append(df1.iloc[indexes])
        # data = pd.concat(df.iloc[indexes])

    

    data = df.where(df1.emotion == 'happy')
    final_sad_arigit = data.dropna()
    print(final_sad_arigit)
    # print(arigitsad_list)


lata_happy()
lata_sad()
arijit_sighn_happy()
arijit_sighn_sad()
jubin_happy()
jubin_sad()