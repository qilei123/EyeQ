import pandas as pd
import os
import glob
import random
def cp_quality(csv_file,quality_label=0):
    quality_des = ['good','usable','reject']
    if "test" in csv_file:
        dataset = "test"
    elif "train" in csv_file:
        dataset = "train"
    else:
        print("No Action!")
        return 

    csv_records = pd.read_csv(csv_file)

    print(csv_records.quality.value_counts())

    for file_name,label in zip(csv_records.image,csv_records.quality):
        if label==quality_label:
            command = "cp /data0/qilei_chen/AI_EYE/kaggle_data/"+dataset+"_/"+file_name+" /data1/qilei_chen/DATA/DB_NATURAL/data3/"+quality_des[int(quality_label)]+"/"
            os.system(command)

def random_split(src_dir,dst_dir,label,ratio=4):
    src_files = glob.glob(os.path.join(src_dir,"*.jpeg"))
    random.shuffle(src_files)
    count=0
    for src_file in src_files:
        count+=1
        command = "cp "+src_file
        if count%(ratio+1)==0:
            command+=" "+dst_dir+"val/"+str(label)+"/"
        else:
            command+=" "+dst_dir+"train/"+str(label)+"/"
        os.system(command)

'''
cp_quality("data/Label_EyeQ_train.csv")
cp_quality("data/Label_EyeQ_test.csv")

cp_quality("data/Label_EyeQ_train.csv",1)
cp_quality("data/Label_EyeQ_test.csv",1)
'''

random_split("/data1/qilei_chen/DATA/DB_NATURAL/data3/good","/data1/qilei_chen/DATA/DB_NATURAL/data3/",0)
random_split("/data1/qilei_chen/DATA/DB_NATURAL/data3/reject","/data1/qilei_chen/DATA/DB_NATURAL/data3/",1)