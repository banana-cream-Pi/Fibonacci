#
import time
def Launch():
    donut = True
    while donut:
        cmd = input("\nInput Command\nType Help For Commands\nCommand: ")
        if cmd.lower() == 'check':
            b = input('\nFibonachi Checker \nInput Number: ')
            a = 0
            i = 0
            stuff = True
            if b.lower() == 'stop' or b == 'cancel':
                donut = False
            try:
                int(b)
                z = int(b)
            except ValueError:
                print('\nPlease input Number\n')
                continue
            while stuff:
                if z == fibonachi_numbers[i]:
                    print('\n'+str(z),'is a Fibonaci number\n<'+('='*(len(str(z))+19))+'>')
                    time.sleep(1)
                    stuff = False
                else:
                    i+=1
                if i == 10000:
                    print('\n'+str(z),'is not Fibonaci number\n<'+('='*(len(str(z))+21))+'>')
                    time.sleep(1)
                    stuff = False
        elif cmd.lower() == 'stop' or cmd.lower() == 'cancel':
                donut = False
                print("Thank You For Useing Fibonachi+\nHave a Nice day\nType 'Launch()' to restart \nType 'Check()' to use only the check Function\nType 'List()' to use only the list function")
        elif cmd.lower() == 'help' or cmd.lower() == 'h':
            print('\nFibonachi +\nVersion-Beta.0.1.0\nCopyright 2019, BCPI Indistries All Rights Reserved')
            print("\nCommands:\n    List =========> lists the Fibonachi sequence\n    Check =========> Checks if the Number you imputed is a Fibonachi number.\n    Stop =========> Stops the program and allows accsess to select commands")
            print('<=========================================================================>\n')
            time.sleep(1)
            continue
        elif cmd.lower() == 'list':
            print('\nFibonachi Lister')
            q = input('How many numbers do you want?(Limit 1000(total database 10000)): ')
            if q.lower() == 'stop' or q.lower == 'cancel':
                donut = False
                print("Thank You For Useing Fibonachi+\nHave a Nice day\nType 'Launch()' to restart \nType 'Check()' to use only the check Function\nType 'List()' to use only the list function")

            try:
                int(q)
                d = int(q)
            except ValueError:
                print('\nPlease input Number\n')
                continue
            if d > 1000:
                print('The Limit is 1000, Please enter something lower than that')
                continue
            for i in range(d):
                print(fibonachi_numbers[i])
            print('<'+('='*(len(str(fibonachi_numbers[d]))-2))+'>')   
            time.sleep(1)
        else:
            print('\nplease input valid command')
    
x = 1
y = 1
fibonachi_numbers = []
while len(fibonachi_numbers)<10000:
       x+=y
       y+=x
       fibonachi_numbers.append(x)
       fibonachi_numbers.append(y)

Launch()

def Check():
    donut = True
    while donut:
        b = input('\nFibonachi Checker \nInput Number: ')
        a = 0
        i = 0
        stuff = True
        if b.lower() == 'stop' or b.lower() == 'cancel':
            donut = False
            print('Thank You')
            continue
        try:
            int(b)
            z = int(b)
        except ValueError:
            print('\nPlease input Number\n')
            continue
        while stuff:
            if z == fibonachi_numbers[i]:
                print(z,'is a Fibonaci number\n<'+('='*(len(str(z))+19))+'>')
                time.sleep(1)
                stuff = False 
                
            else:
                i+=1
            if i == 10000:
                print(z,'is not Fibonaci number\n<'+('='*(len(str(z))+21))+'>')
                time.sleep(1)
                stuff = False
def List():
    donut = True
    while donut:
        print('\nFibonachi Lister')
        q = input('How many numbers do you want?(Limit 1000(total database 10000)): ')
        if q.lower() == 'stop':
            donut = False
            print('Thank You')
            continue
        try:
            int(q)
            d = int(q)
        except ValueError:
            print('\nPlease input Number\n')
            continue
        if d > 1000:
            print('The Limit is 1000, Please enter something lower than that')
            continue
        for i in range(d):
            print(fibonachi_numbers[i])
        print('<'+('='*(len(str(fibonachi_numbers[d]))-2))+'>')
        time.sleep(1)
