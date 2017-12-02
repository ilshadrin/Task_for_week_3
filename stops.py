

import csv


dict1={}
with open('stop_1.csv', 'r', encoding='windows-1251') as f:
    fields = ['Name', 'Street']
    #fields = ['Name', 'Street']
    reader = csv.DictReader(f, fields, delimiter=',')
    street_count=[]
    #print(street_count)


    for line in reader:
        #print(line['Name'], line['Street'])    
        #print(line, type(line))    # type(line) - определяет тип переменной, в данном случае это словарь
        #print(line['Street'])
        #a=line['Street']
        street_count.append(line['Street']) # общий список только с улицами

        if  line['Street'] in dict1:
            dict1[line['Street']]+=1
        else:
            dict1[line['Street']]=1


print(sorted(dict1.items(), key=lambda x:x[1]) [-5:]) #выдает 5 последних улиц с максимом остановок

# dict1.items() - создание списка кортежей(мега большой словарь, первый элемнет ключ, второй словарь, в них всегда 2 элемента)
# sorted -сортировка списка кортежей ( что сортируем, параметр сортировки)
#key - ключ сортировки lambda- шаблонная неопределенная функция, сортируем по х:x[1]- по второму элементу в кортеже, сортировка по возрастанию

#[-5:] - вывести 5 последних элементов


#print(street_count, type(street_count))    # общий список только с улицами


#считает улицу с максимумом остановок, но не очень верно

max_value_stop=0

for stop_name in street_count:
    present_number=street_count.count(stop_name)

    if present_number>max_value_stop:
        max_value_stop=present_number
        itog=stop_name
    

print('maax nuber stop ',max_value_stop)
print('name max number stop', itog)

