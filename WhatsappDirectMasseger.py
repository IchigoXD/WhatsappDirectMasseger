import os
from time import sleep
import webbrowser  
os.system('cls')


WAdomain = "https://wa.me/"
print('\n')
number = input("What is the number that massege want to send?  \n> ")
print('\n')
isthisLocal = True if input('Is this number Local? (Yes/No) \n> ').capitalize() == 'Yes' else False
print('\n')

if number[0]=='0' and number[1]=='0':
    WAnumber = '+' + number[2:]
elif number[0]=='0' and isthisLocal:
    Ccode = input('Enter your contry code. Like this +81 , +94 \n> ')
    WAnumber = Ccode + number[1:]
elif number[0]=='+':
    WAnumber = number
else:
    print('This is not a phone number..!')
    exit()
    
  

url = WAdomain + WAnumber  
print(url)
webbrowser.open_new_tab(url)

sleep(5)

exit()
