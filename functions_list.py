phonebook = {
'Jack': '555-555-5555', 
'Jill': '543-321-1234', 
'Diane': '123-321-4321', 
}
def border():
    line ='================================='
    return line

def main_menu():
    print 'Welcome to the phone book app.'
    print border()
    print '1. Look up an entry '
    print '2. Set an entry '
    print '3. Delete an entry '
    print '4. List all entries '
    print '5. Quit '

def response_one():
    print border()
    lookup = (raw_input('Who would you like to look up?'))
    if lookup in phonebook:
        print phonebook[lookup]
    else:
        print 'Sorry that name is not in the phonebook.'

def response_two():
    print border()
    print 'Please enter info for new: entry '
    new_name = (raw_input('Name: '))
    new_phone = (raw_input('Phone Number: '))
    phonebook[new_name] = new_phone
    new_name = ''
    new_phone = ''

def response_three():
    print border()
    remove_question = (raw_input('What name would you like to remove?'))
    if remove_question in phonebook:
        prompt = (raw_input('Are you sure you want to remove (y/n)'))
        print phonebook[remove_question]
        if prompt.lower() == 'y':
            del phonebook[remove_question]
        elif prompt.lower() == 'n':
            print 'Ok I will return you to the menu.'
    elif remove_question not in phonebook: 
        print 'That is not a valid entry. Returning to Main Menu.'

def response_four():
    print border()
    print phonebook

