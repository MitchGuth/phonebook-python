import functions_list

while True:
    functions_list.main_menu()
    choice = raw_input('What do you want to do?' )
    response = int(choice)
    if response == 1:
        functions_list.response_one()
    elif response == 2: 
        functions_list.response_two()
    elif response == 3: 
        functions_list.response_three()
    elif response == 4:
        functions_list.response_four()
    elif response == 5: 
        print functions_list.border()
        print 'Have a great rest of your day!'
        break
    else:
        print functions_list.border()
        print 'Unfortunately, that was not an integer 1-5.'
        break