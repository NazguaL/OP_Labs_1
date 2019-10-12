# Создать Console-приложение:
# Для всех вариантов обязательными методами есть Read, ReadLine, ReadKey, Write().
# Вариант 1 (16): BackgroundColor, CapsLock

#text = input("Введіть будь який текст: ")
#print('Ви ввели наступний текст: ' + text)

import subprocess
import os
from termcolor import colored
import colorama
from colorama import Back as bg
from colorama import Fore as fr
from colorama import Fore, Back, Style

if subprocess.check_output('xset q | grep LED', shell=True)[65] == 50 :
    capslock = False
if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51 :
    capslock = True
# https://stackoverflow.com/questions/13129804/python-how-to-get-current-keylock-status
print("capslock ON is : ", capslock)
print(colored('hello', 'red'), colored('world', 'green'))



colorama.init()
print(bg.RED)
print(bg.RED)
print(fr.RED)
print(colorama.ansi.clear_screen())


print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

