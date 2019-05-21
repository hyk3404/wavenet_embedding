import pandas as pd
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from file_load import file_path,folder_path

path = './dataset'
name = '_OK.npy'
    
file_list, file_name = file_path(path, name)

features_list = []

for npy in file_list:
    feature = np.load(npy)
    features_list.append(feature)

features_array = np.array(features_list)

cos_sim_features = cosine_similarity(features_array)
df_cos_sim = pd.DataFrame(cos_sim_features,index = file_name, columns = file_name)

for music_name, path in zip(file_name, file_list):
    sort = df_cos_sim[music_name].sort_values(ascending=False)
    sort_20 = pd.DataFrame(sort.head(10))

    sort_20.to_csv(path.replace('.npy', '')+'.csv')
    print(path.replace('.npy', '')+'.csv')


# print(df_features)

# euc_dis = euclidean_distances(features_array)

# df_features = pd.DataFrame(euc_dis,index = file_name, columns = file_name)

