import os

def show_records(records_dir):

    records = open(records_dir)

    line = records.readline()

    counts = []
    count = 0
    while line:
        count+=1

        label = int(line[-2])

        if label>=len(counts):
            counts.append(1)
        else:
            counts[label]+=1

        line = records.readline()

    print(count)
    print(counts)

projects = {"binary":[0,1],"multilabel":[0,1,2,3,4,5]}
model_names = ["vgg11","densenet121","inception3"]

for key in projects:
    for model_name in model_names:
        for label in projects[key]:
            records_dir = os.path.join("/data1/qilei_chen/DATA/gastro",key,model_name,"best.model_"+str(label)+".txt")
            show_records(records_dir)
#show_records("/data1/qilei_chen/DATA/gastro/binary/vgg11/best.model_0.txt")
#show_records("/data1/qilei_chen/DATA/gastro/binary/vgg11/best.model_1.txt")