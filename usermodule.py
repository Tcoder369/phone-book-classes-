from time import sleep

class Person:
    def __init__(self, group, phone_number, adress):
        self.group = group
        self.phone_number = phone_number
        self.adress = adress

    def __repr__(self):
        return self.phone_number + ", " + self.adress + ", is in group - " + self.group + ','

groups = ['family', 'friends', 'work', 'school', 'other']
people = {}

print('welcome to your automated phone book!\n')
sleep(4)
while True:
    print('what would you like to do:')
    print('[a] find an individuale contat')
    print('[b] look at an entire group of contacts')
    print('[c] add a contact to your phone book')
    print('[d] remove a contact from your phone book')
    print('[e] delete amount of contacts by group')
    print('[f] see your entire phone book')
    print('[g] edit a contact\n')
    action = input()

    #done
    if action == 'a':
        to_print = []
        detail = input('\ninsert person\'s name, adress or phone number: ')
        sleep(4)
        found = False
        for person in people.keys():
            if person == detail and person not in to_print:
                to_print.append(person)
                
            if people.get(person).adress == detail and person not in to_print:
                 to_print.append(person)
                 
            if people.get(person).phone_number and person not in to_print:
                to_print.append(person)

        if len(to_print) == 0:
            print('\nwe are sorry but we didn\'t find a person with detail ' +
                  detail + ' in your phone book.\n')
        else:
          for i in to_print:
            print('\n', i, '\n', people.get(i), '\n')
        sleep(4)

    #done
    elif action == 'b':

        group = input(
            '\nwhich group would you like to look at, \noptions are:\n' +
            str(groups) + ": ")
        sleep(4)
        for thing in groups:
            if group == thing:
                found = True
                break
            else:
                found = False
        while found == False:
            print('\nno such group in your phone book')
            group = input(
                '\nwhich group would you like to look at, \noptions are:\n' +
                str(groups) + ": ")
        printable = []
        for person in people:
            if people.get(person).group == group:
                printable.append(person)
        if len(printable) > 0:
            for i in printable:
              print('\n', i, '\n', people.get(i), '\n')
        else:
            print('\nthis group is empty\n')
        sleep(4)

    #done
    elif action == 'c':

        name = input('\nwhat is the name: ')

        while name in people.keys():
            print(
                '\nyou already have someone called ' + name +
                ' in your phone book if you are trying to change this persons information please select that action in the main menu.\n'
            )
            name = input('\nwhat is the name:')
        group = input('\nwhat group do you want ' + name +' in \noptions are ' + str(groups) + ': ')

        while group not in groups:
            group = input('\nwhat group do you want ' + name + ' in \noptions are ' + str(groups) + ': ')
        phone_number = input('\nwhat is ' + name + '\'s phone number: ')
        for person in people:
          while phone_number == people.get(person).phone_number:
            print(person + ' already has this phone number: ' + str(phone_number)+ ' please make sure you are putting in the correct phone number or go back to the main menu to change ' + person + '\'s phone number')
            phone_number = input('\nwhat is ' + name + '\'s phone number: ')

        adress = input('\nwhat is ' + name + '\'s adress: ')
        people[name] = Person(group, phone_number, adress)
        print('\n', name, 'has been added succesfuly to your phone book.\n')
        sleep(4)

    #done
    elif action == 'd':
        detail = input('\ngive us the name of the person you would like to remove: ')
        found = False
        available = []
        for person in people.keys():
            if person == detail:
                available.append(person)

        if len(available) < 1:
            print('\nno one in your phone book called ' + detail + '\n')
        elif len(available) == 1:
            inputr = input('\nare you sure you want to delete ' + detail + '? [y/n] (lower case please) ')
            while inputr != 'y' and inputr != 'n':
              inputr = input('\nare you sure you want to delete ' + detail + '[y/n] (lower case please) ')
            if inputr == 'y':  
              print('\nwe will be deleting ' + str(available) + ' shortly.')
              print('\n', detail, people.pop(available[0]))
              print('\nhas been deleted from your phone book\n')
            elif inputr == 'n':
              print('\naction has been cancled we will not be deleting ' + detail + 'from your phone book\n')
            sleep(4)

    #done
    elif action == 'e':
        group = input('\nwhich group would you like to delete: ')
        to_remove = []
        for i in people:
            if people.get(i).group == group:
                to_remove.append(i)
        if len(to_remove) == 0:
            print('\nno one in group ' + group + ' in your phone book\n')
        else:
            print('\nwe are removing these people...')
            for i in to_remove:
                print('\n', i, people.pop(i))

            print('group ' + group +
                  ' has been deleted from your phone book\n')
        sleep(4)

    #done
    elif action == 'f':
        print('\n')
        if len(people) < 1:
            print('no one in your phone book yet\n')
        else:
            for i in people:
                print(i, '\n', people.get(i), '\n')
        sleep(4)

    #done
    elif action == 'g':
        can_be_changed = ['name', 'group', 'phone number', 'adress']
        person = input('\nwho\'s info would you like to change: ')
        to_change = []
        for thing in people.keys():
            if thing == person:
                to_change.append(thing)
        if len(to_change) > 0:
            
          change = input('\nwhat would you like to change options are \n[name, group, phone number, adress]: ')
       
          while change not in can_be_changed:
            change = input('\nwhat would you like to change options are \n[name, group, phone number, adress]: ')

          if change == 'name':
            print('\ncurrent name is ' + person)
            new = input('\nwhat new name would you like to give ' + person + ':')
            people[new] = people[to_change[0]]
            del people[to_change[0]]
            print('\nname has been successfuly changed to ' + new)
          elif change == 'group':
            print('\n',person + '\'s current group is '+ people.get(person).group)
            new = input('\nwhat group would you like ' + person + 'to be in options are ' + str(groups) + ':')
            people[to_change[0]].group = new
            print('\ngroup has been successfuly changed to ' + new)
          elif change == 'phone number':
            print('\n', person + '\'s current phone number is '+ people.get(person).phone_number)
            new = input('\nwhat new phone number would you like to give '+ person + ':')
            people[to_change[0]].phone_number = new
            print('\nphone number has been successfuly changed to ' + new)
          elif change == 'adress':
            print('\n',person + '\'s current adress is '+ people.get(person).adress)
            new = input('\nwhat new adress would you like to give ' + person+ ':')
            people[to_change[0]].adress = new
            print('\nadress has been successfuly changed to ' + new)

        else:
          print('\nno one in your phone book with name ' + person + '\n') 
        sleep(4)

    #done
    else:
        print('\nno such action available\n')
