import os
import shutil

dir_list = ['./dataset/train/', './dataset/test/']

for dir in dir_list:
    if not os.path.exists(dir):
        os.makedirs(dir)
        
def dataset_split(query):
    for dir in dir_list:
        os.makedirs(dir+query, exist_ok=True)
        
    cnt = 0
    train_cnt = int(len(os.listdir(query))*0.7)
    for file_name in os.listdir(query):
        if cnt < train_cnt:
            shutil.move(query+'/'+file_name, dir_list[0]+query+'/'+file_name)
        else:
            shutil.move(query+'/'+file_name, dir_list[1]+query+'/'+file_name)
        
        cnt += 1
        
    shutil.rmtree(query)
    
data = input()
dataset_split(data)