
import time
from selenium import webdriver
from pynput.keyboard import Key, Controller
import termcolor


print('░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗')
print('░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝')
print('░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░')
print('░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░')
print('░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗')
print('░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝')
print('         ')

print('Instructions:\nnavigate to text conversation input bar')
print('         ')
print('Enter message to send:')
spam_text = str(input())
print('         ')
print(termcolor.colored('you have 10 seconds to navigate to target conversation after inputing # of messages', 'red', 'on_grey'))
print('How many messages?:')
messages = int(input())
print('         ')
print('Do not interact with keyboard')
for i in range(1,11):
    time.sleep(1)
    print(str(i))

keyboard = Controller()

time.sleep(3)
for i in range(messages):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    for x in list(spam_text):
        time.sleep(.02)
        keyboard.type(x)
