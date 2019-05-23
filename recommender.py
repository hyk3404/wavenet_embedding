from file_load import file_path
import pandas as pd
import numpy as np

def recommend(music_path,music_name):
    # cos_list, cos_name, folder_list, folder_name = file_path('./dataset', '_cos.csv')
    # euc_list, euc_name, folder_list, folder_name = file_path('./dataset', '_euc.csv')
    recommend_list=[]
    for mp3_path in music_path:
        cos = pd.read_csv(mp3_path.replace('.npy', '_cos.csv'))
        cos = cos.iloc[1:,0:1].values.tolist()

        for i in range(len(cos)):
            cos[i]=cos[i][0]

        euc = pd.read_csv(mp3_path.replace('.npy', '_euc.csv'))
        euc = euc.iloc[1:,0:1].values.tolist()

        for i in range(len(cos)):
            euc[i]=euc[i][0]

        ret = list(set(cos).intersection(set(euc)))
        ret = list(set(ret).difference(set(music_name)))

        if len(ret)>=2:
            ret = ret[0:2]
        
        else:
            ret = list(set(euc).difference(set(music_name)))
            ret = ret[0:2]

        recommend_list += ret
    
    # print(len(recommend_list))
    
    return recommend_list

# if __name__ == "__main__":
#     file_list, file_name, folder_list, folder_name = file_path('./dataset', '_OK.npy')
#     recommend(file_list,file_name)
