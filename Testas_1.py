task_list = {}
completed_task_list = {}

#task = key
#data = value


def option1():
    task = input('Write a task that you would like to add: ').lower()
    date = input('Add due date: ').lower()
    task_list[task] = date
    print(task_list)


def option2():
    x = 0
    print('\nTASK LIST:')
    for key, value in task_list.items():
        x += 1
        print(f'{x}. {key} (due {value})')


def option3():
    delete_task = input('Write the name of the task that you want to delete: ').lower()
    if delete_task in task_list:
        del task_list[delete_task]
        option2()
    elif delete_task in completed_task_list:
        print('This task has already been completed.')
    else:
        print('This task is not in the task list. Try again.')
        option3()


def option4():
    completed_task = input('Write the name of the completed task: ').lower()
    if completed_task in task_list:
        completed_task_list['✓ ' + completed_task + ' ✓'] = task_list[completed_task]
        task_list['✓ ' + completed_task + ' ✓'] = task_list.pop(completed_task)
        option2()


def option5():
    dump = []
    search = input('Search: ').lower()
    for key, value in task_list.items():
        if key in search:
            dump.append(search)
            print(f'{key} (due {value})')
        elif value in search:
            dump.append(search)
            print(f'{key} (due {value})')
        elif search in key:
            dump.append(search)
            print(f'{key} (due {value})')
        elif search in value:
            dump.append(search)
            print(f'{key} (due {value})')
    if not dump:
        print('No search results.')



def option6():
    task = input('Write the name of the task that you want to edit: ').lower()
    if task in task_list:
        name_date = input('Would you like to edit the name or the date? ').lower()
        if name_date == 'name':
            new_name = input('Write new name: ').lower()
            task_list[new_name] = task_list.pop(task)
            option2()
        elif name_date == 'date':
            new_date = input('Write the new date: ')
            task_list[task] = new_date
            option2()


def option7():
    x = 0
    print('\nCOMPLETED TASK LIST:')
    for key, value in completed_task_list.items():
        x += 1
        print(f'{x}. {key} (due {value})')


def main():
   while True:
       print("\nTo-Do List Options:")
       print("1. Add task")
       print("2. Display tasks")
       print("3. Delete task")
       print("4. Mark task as completed (BONUS)")
       print("5. Search task (BONUS)")
       print("6. Edit task (BONUS)")
       print("7. Display completed tasks")
       print("8. QUIT")
       try:
           option = int(input('Enter your choice: '))
           if option == 1:
               option1()
           elif option == 2:
               option2()
           elif option == 3:
               option3()
           elif option == 4:
               option4()
           elif option == 5:
               option5()
           elif option == 6:
               option6()
           elif option == 7:
               option7()
           elif option == 8:
               print('Exiting task list!')
               exit()
           else:
               print('Invalid option. Please enter a number between 1 and 6.')
       except ValueError:
           print('Please enter a number.')
main()

#Noreciau dar ilgiau pasedeti, nes azartas paeme viska padaryti graziai ir kaip turi buti, bet dar labiau miego noriu. :D Gero taisymo!
