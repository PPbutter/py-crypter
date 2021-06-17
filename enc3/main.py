import encryptr, time, os
from encryptr import red,reset,blue,green,purple,lightWhite,lightBlue,yellow,bold,normal

try:
    from terminaltables import DoubleTable
except ModuleNotFoundError:
    install = ["install","terminaltables"]
    import pip
    pip.main(install)


key = ""

keyStatus = 0

command = [["\033[1;36m\n\n\n\n\n\n\n\nCOMMANDS\n", """
encrypt  :  Encrypt the inputed file


decrypt  :  Decrypt the inputed file


key      :  Enter the name of the key file in the key folder


testkey  :  Test the key you selected is correct and working (WIP)


cwd      :  gets your current working directory


terminal :  emulates terminal


exit     :  Exits the app.\n\033[1;m""","\n\n\n\n\n\n\n\nSYMBOLS\n",f"""
{yellow}[{red}!{yellow}]{lightBlue} : Warning



{reset}[{lightBlue}?{reset}]{lightBlue} : Question



{reset}[{red}?{reset}]{lightBlue} : Important question



{reset}[{green}+{reset}]{lightBlue} : Positive responce



{reset}[{red}-{reset}]{lightBlue} : Negative responce"""]]

def terminalmode():
    usr = os.getlogin()
    while True:
        prompt1 = input(f"{blue}{bold}{usr} @ cryptr{green} ➮{reset}{normal}{purple}  ")
        print(reset)
        print(normal)
        if prompt1 == "exit":
            break
        else:
            pass
        os.system(f"{prompt1}")

def getkey():
    x = input(f"\n{reset}{bold}[{blue}?{reset}]{lightWhite}do you already have a key generated?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
    print(reset,normal)
    if x == "1":
        global key
        global keyStatus
        global fs
        print(f"{reset}{bold}{yellow}[{red}!{yellow}]{reset} BE SURE TO INCLUDE THE EXTENTIONS example: .key or .txt{reset}\n")
        print(f"\n{reset}{bold}{yellow}[{red}!{yellow}]{reset} BE SURE THE FILE IS IN THE \\key DIRECTORY{reset}\n")
        fs = input(f"\n{bold}[{blue}?{reset}]{lightWhite} what is the name of the file that contains the key?:{lightBlue} ")
        print(reset,normal)
        key = encryptr.get_key(fs)
        keyStatus = 1
        print(f"{bold}[{green}+{reset}]{lightWhite} key selected{reset}\n")
    
    if x == "2":
        global asa
        y = input(f"{reset}{bold}[{blue}?{reset}]{lightWhite} would you like to generate a key?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
        if y == "1":
            print(f"\n{reset}{bold}{yellow}[{red}!{yellow}]{reset} BE SURE TO INCLUDE THE EXTENTIONS i.e. .key or .txt{reset}\n")
            asa = input(f"{reset}{bold}[{blue}?{reset}]{lightWhite}what would you like to name the file?: ")
            encryptr.gen_key(asa)
            time.sleep(1)
            print(f"\n{reset}{bold}[{green}+{reset}]{lightWhite} key generated{reset}\n")
            asdas = input(f"{reset}{bold}[{blue}?{reset}]{lightWhite} would you like to select the key you had just generated?{reset}\n{lightWhite}1){reset} {green}yes{reset}\n{lightWhite}2){reset} {red}no{reset}\n{lightWhite}->{reset}{lightBlue} ")
            if asdas == "1":
                key = encryptr.get_key(asa)
                print(f"\n{reset}{bold}[{green}+{reset}]{lightWhite} key selected{reset}\n")
                keyStatus = 1
            elif asdas == "2":
                print("ok just rerun the command to select your key")
        elif y == "2":
            print("ok the app will now exit")
            exit()

def encrypt():
    if keyStatus == 0:
        print(f"\n{bold}{yellow}[{red}!{yellow}]{lightWhite} please select your key file first. enter the command: {blue}key{reset}{normal}\n")
        return
    elif keyStatus == 1:
        pass
    xc = input(f"\n{reset}{bold}[{blue}?{reset}]{lightWhite} what is the file name?:{lightBlue} ")
    xcv = input(f"\n{reset}{bold}[{blue}?{reset}]{lightWhite} what would you like the new file to be called?:{lightBlue} ")
    encryptr.enc(key,xc,xcv)
    time.sleep(0.5)
    encryptr.MoveEncFile(xcv)

def decrypt():
    if keyStatus == 0:
        print(f"\n{bold}{yellow}[{red}!{yellow}]{lightWhite} please select your key file first. enter the command: {blue}key{reset}{normal}\n")
        return
    elif keyStatus == 1:
        pass
        zxc = input(f"{reset}{bold}[{blue}?{reset}]{lightWhite} what is the file name?:{lightBlue} ")

        zcv = input(f"{reset}{bold}[{blue}?{reset}]{lightWhite} what would you like the new file to be called?:{lightBlue} ")
        encryptr.deenc(key,zxc,zcv)
        time.sleep(0.5)
        a = encryptr.MoveDeencFile(zcv)   

def makefolders(check1):
    encryptr.make_folders(check1)

def cwdd():
    cwd = os.getcwd()
    return cwd

def testkey():
    if keyStatus == 1:
        try:
            f = encryptr.Fernet(key)
        except ValueError:
            print(print(f"{reset}{bold}{yellow}[{red}!{yellow}]{reset}{lightWhite} the key file you entered was not 32 url-safe base64-encoded bytes{reset}\n"))
        if key is not None:
            try:
                print(f"\n{bold}{lightWhite}file you selected: {bold}{blue}{fs}{reset}\n\nyour key is: {bold}{blue}{key}\n")
            except NameError:
                print(f"\n{bold}{lightWhite}file you selected: {bold}{blue}{asa}{reset}\n\nyour key is: {bold}{blue}{key}\n")
    if keyStatus == 0:
        print(f"\n{bold}{yellow}[{red}!{yellow}]{lightWhite} please select your key file first. enter the command: {blue}key{reset}{normal}\n")

makefolders(0)
commands = ["help","encrypt","decrypt","key","testkey","cwd","terminal","exit"]
x = DoubleTable(command,)
table = x.table
print(table)
def funcy(commands, table):
    prompt = input(f"{blue}{bold}cryptr{green} ➮{reset}{normal}{purple}  ")
    if prompt == commands[0]:
        print(f"{reset}{table}")
    elif prompt == commands[1]:
        encrypt()
    elif prompt == commands[2]:
        decrypt()
    elif prompt == commands[3]:
        getkey()
    elif prompt == commands[4]:
        testkey()
    elif prompt == commands[5]:
        sa = cwdd()
        print(f"\n{reset}{bold}[{green}+{reset}]{lightWhite} your cwd is: {blue}{sa}{reset}\n")
    elif prompt == commands[6]:
        terminalmode()
    elif prompt == commands[7]:
        exit(f"\n\n{reset}{bold}bye have a good day (^_^)/\n{normal}")

while True:
    try:
        funcy(commands, table)
    except KeyboardInterrupt:
        exit(f"\n\n{reset}{bold}bye have a good day (^_^)/\n{normal}")
    except FileNotFoundError:
        print(f"{reset}{bold}{yellow}[{red}!{yellow}]{reset} sorry the file you entered was not found\n")
    finally:
        pass