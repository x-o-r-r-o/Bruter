#Need:
#pip3 install colorama
#pip3 install rarfile
#pip3 install pyzipper

import os, sys, time, pyzipper
from rarfile import RarFile 
from colorama import Fore
from zipfile import ZipFile

isBruted = False
dictionName = 'Files'
start = time.time ()
platform = ''

def clear ():
    if os.name == 'nt':
        _ = os.system ('cls')
    else:
        _ = os.system ('clear')

def getArchiveInfo (diction, archive):
    with open (archive, 'rb') as file:
        currentType = file.read(2).decode()
      
    if currentType == 'PK':
        bruteZip (diction, archive)  

    elif currentType == 'Ra':
        bruteRar (diction, archive)

    else:
        print (Fore.YELLOW + 'Такой формат не поддерживается :(')


def bruteZip (diction, archive):
    global isBruted, dictionName, platform
    passwords = open (diction).read().splitlines()
    if platform == 'win32':
        with pyzipper.AESZipFile (archive) as zArchive:
            for password in passwords:
                if isBruted == False:
                    try:
                        zArchive.setpassword (password.encode ())
                        zArchive.extractall (dictionName)
                        isBruted = True
                        print (Fore.GREEN + '[+] Password is ' + password)
                    except:
                        print (Fore.    RED  + '[+] Password is not ' + password)
                else:
                    finish()

    elif platform == 'linux':
        with ZipFile (archive) as zArchive:
            for password in passwords:
                if isBruted == False:
                    try:
                        zArchive.extractall (dictionName, pwd = password.encode())
                        isBruted = True
                        print (Fore.GREEN + '[+] Password is ' + password)
                    except:
                        print (Fore.RED + '[+] Password is not ' + password)
                else:
                    finish()

def bruteRar (diction, archive):
    global isBruted, dictionName
    passwords = open (diction).read().splitlines()
    rArchive = RarFile (archive)
    for password in passwords:
        if isBruted == False:
            try:
                rArchive.extractall (path = dictionName, pwd = password)
                isBruted = True
                print (Fore.GREEN + '[+] Password is ' + password)
            except:
                print (Fore.RED  + '[+] Password is not ' + password)
        else:
            finish()

def finish ():
    print (Fore.RESET + 'Спасибо, что читаете @Termuxtop')
    end = time.time ()
    print ('Времени ушло -> {}'.format (end-start) + ' секунд')
    sys.exit()
        

def main ():
    global dictionName, platform
    print('''
Разработчики: @sudoTulpa и @nkitas
Наш телеграмчик: @Termuxtop
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .▄▄▄  
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·▀▄ █·
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄▐▀▀▄ 
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌▐█•█▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ .▀  ▀
[1] -> Linux (Termux)
[2] -> Windows
    ''')

    platform = input ('Выберите платформу, где БЫЛ СОЗДАН архив: ')

    if platform == '1':
        platform = 'linux'
    elif platform == '2':
        platform = 'win32'
    else:
        print (Fore.YELLOW + 'Ваша платформа не поддерживается :(')
        sys.exit ()

    diction = input ('Название файла с паролями: ')
    archive = input ('Название архива: ')

    try:
        os.mkdir (dictionName)
    except FileExistsError:
        pass

    getArchiveInfo (diction, archive)

if __name__ == '__main__':
    clear ()
    main ()