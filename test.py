
import os

PATH_MODELS = 'forecastdss/models/'
PATH_LOCAL = '/local_storage'

def save_model_local(country):
    file_train = 'train.pkl'
    foldername = PATH_MODELS + country
  
    path_local = os.path.join(foldername, file_train)
    path_local = path_local.replace("\\", "/")
    
    return path_local
  
local = save_model_local('CL')  
print(local)
