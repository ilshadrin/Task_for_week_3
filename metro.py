import json

with open('metro.json', 'r', encoding='windows-1251') as f:
    read=json.load(f) #получаем данный из файла json
    #print(read)

count=0
for a in read:

    if a['RepairOfEscalators']:
        print('станция ', a['NameOfStation'])
        count+=1


print(count)

