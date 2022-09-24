thoughts = []

def your_thoughts():
    while True:
        try:
            selection = int(input('choose 1, 2, or 3: '))
            if(selection > 0 or selection < 4):
                while True:
                    if(selection == 1):
                        your_thought = input("your thoughts will be stored: ")
                        thoughts.append(your_thought)
                        if(thoughts != None):
                            ask_user = input("another thought?(y or n) ")
                            if(ask_user == 'n'):
                                break
                        
                    elif(selection == 2):
                        print('this is your thoughts so far: ')
                        read_thoughts(thoughts)
                    elif(selection == 3):
                        print('good bye for now')
                        break
                break
            else:
                selection = 'error'
                print('you didnt choose within the range of number, so try again')
        except ValueError:
            print("you're a creative one, try again")
    return selection





def read_thoughts(thoughts):
    for thought in thoughts:
        print(thought)

your_thoughts()