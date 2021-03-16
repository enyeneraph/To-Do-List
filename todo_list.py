todo_list = [('TITLE', 'TIME')]

print('Type yes below if you would like to create a to-do list')
response = input()

while response.lower() == 'yes':
    item = input('Add item\n')
    schedule = input('Add a schedule for your item\n')
    todo_list.append((item, schedule))
    print('')
    print('YOUR TO-DO LIST'.center(40))
    for i, j in todo_list:
        print(i.ljust(20)+j.rjust(20))
    print('')
    response = input('Type yes if you would like to add another item\n').lower()
    
