import pandas as pd
import os

def cp_reject(csv_file):

    if "test" in csv_file:
        dataset = "train"
    elif "train" in csv_file:
        dataset = "test"
    else:
        print("No Action!")
        return 

    csv_records = pd.read_csv(csv_file)

    print(csv_records.quality.value_counts())

    for file_name,label in zip(csv_records.image,csv_records.quality):
        if label==2:
            command = "cp /data0/qilei_chen/AI_EYE/kaggle_data/"+dataset+"_ "+file_name+" /data1/qilei_chen/DATA/DB_NATURAL/data3/rejects/"
            os.system(command)
cp_reject("data/Label_EyeQ_train.csv")
cp_reject("data/Label_EyeQ_test.csv")