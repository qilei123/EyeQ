import pandas as pd
import os

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
cp_quality("data/Label_EyeQ_train.csv")
cp_quality("data/Label_EyeQ_test.csv")

cp_quality("data/Label_EyeQ_train.csv",1)
cp_quality("data/Label_EyeQ_test.csv",1)