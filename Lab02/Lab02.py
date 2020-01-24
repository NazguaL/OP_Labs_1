# Создать Console-приложение:
# Для всех вариантов обязательными методами есть Read, ReadLine, ReadKey, Write().
# Вариант 1 (16): BackgroundColor, CapsLock



import subprocess
import colorama
from colorama import Fore, Back, Style

if subprocess.check_output('xset q | grep LED', shell=True)[65] == 50:
    capslock = False
if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51:
    capslock = True
# https://stackoverflow.com/questions/13129804/python-how-to-get-current-keylock-status
print("capslock ON is : ", capslock)

colorama.init()
print(Back.RED)

print(Fore.RED + 'some red text')
print(Style.BRIGHT + Back.GREEN + Fore.RED + 'and with a green background' + Style.RESET_ALL)
print('back to normal now')

