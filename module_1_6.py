my_dict={'Roman': 35,'Coni': 30,'Veronica': 5}
print(my_dict)
my_dict['Anton']=40
print(my_dict.get('Granny','такой даты нет'))
print(my_dict['Roman'])
print(my_dict)
my_dict.update({'Vlad':3,'Kailas':7})
print('обновленное множество',my_dict,)
print('удаленный элемент', my_dict.pop('Roman'))
print(my_dict)

my_set={1,2,5,6,7,8,9,10,1,10,5,4}
my_set=set(my_set)
print(my_set)
my_set_1={999,888}
my_set.update(my_set_1)
print(my_set)
my_set.remove(999)
print(my_set)




